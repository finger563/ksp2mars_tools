// High level controller for vehicle ascent mode.
@lazyglobal off.

// Here is where constants for accessing members of the
// controller context should be defined.
global ctlascctx_logctx is 0.
global ctlascctx_mode is 1.

// Ascent controller flight modes
global ctlasc_mode_preflight is 0.   // Mode before takeoff
global ctlasc_mode_vertical is 1.    // Vertical ascent
global ctlasc_mode_gravturn is 2.    // Gravity turn
global ctlasc_mode_circ is 3.        // Orbit circularization

// Load up helper function library
run ctlasc_util.

// Initialize the ascent library for the vessel state vector
function ctlasc_init {
    declare parameter statevec.
    declare parameter logctx.
    
    return list(logctx, ctlasc_mode_preflight).
}.


// Run the ascent control library for one iteration.
// The return value is the next controller that should be run,
// which will normally be this one until it's finished.
function ctlasc_exec {
    declare parameter ctx.
    declare parameter statevec.
    
    // Some real cacluation should be done to update this flag.
    local transition_to_orbit is false.

    // Run ascent controller state machine
    if ctx[ctlascctx_mode] = ctlasc_mode_preflight) {
        // This is a ground mode so it's permitted to hold up the controller here
        // while doing things sequentially. One of the few places this is permitted.
        
        // Run preflight checks/setup
        ctlasc_preflight(ctx).

        // Start engines
        ctlasc_engine_ignite(ctx).

        // Release launch clamps
        cltasc_release_clamps(ctx).

        // Transition to vertial ascent
        set ctx[ctlascctx_mode] to ctlasc_mode_vertical.
    }
    else if ctx[ctlascctx_mode] = ctlasc_mode_vertical) {
        // Run high level trajectory control (calculate attitude/speed setpoints)
        ctlasc_trajectory_control(ctx, statevec)

        // Run gain scheduling
        ctlasc_schedule_gains(ctx, statevec).

        // Calculate controller outputs
        ctlasc_run_pids(ctx, statevec).

        // Set actuators based on controller outputs
        ctlasc_set_actuators(ctx, statevec).

        // Altitude/speed based calculation here?
        local start_gravturn is false.
        // Transition to gravity turn if ready.
        if start_gravturn {
            set ctx[ctlasctx_mode] to ctlasc_mode_gravturn.
        }.
    }
    else if ctx[ctlascctx_mode] = ctlasc_mode_gravturn) {
        // Run high level trajectory control (calculate attitude/speed setpoints)
        ctlasc_trajectory_control(ctx, statevec)

        // Run gain scheduling
        ctlasc_schedule_gains(ctx, statevec).

        // Calculate controller outputs
        ctlasc_run_pids(ctx, statevec).

        // Set actuators based on controller outputs
        ctlasc_set_actuators(ctx, statevec).

        // Altitude/speed based calculation here?
        local start_circ is false.
        // Transition to gravity turn if ready.
        if start_circ {
            set ctx[ctlasctx_mode] to ctlasc_mode_circ.
        }.
    }
    else if ctx[ctlascctx_mode] = ctlasc_mode_circ) {
        // Run high level trajectory control (calculate attitude/speed setpoints)
        ctlasc_trajectory_control(ctx, statevec)

        // Run gain scheduling
        ctlasc_schedule_gains(ctx, statevec).

        // Calculate controller outputs
        ctlasc_run_pids(ctx, statevec).

        // Set actuators based on controller outputs
        ctlasc_set_actuators(ctx, statevec).

        // Altitude/speed based calculation here?
        set transition_to_orbit to false.
    }.
    
    // If ready to transition to the orbit controller, return the orbit mode flag
    if transition_to_orbit {
        return ctlmode_orbit.
    }.

    // Otherwise return normally
    return ctlmode_ascent.
}.

// Run trajectory calculations to set attitude/speed setpoints
function ctlasc_trajectory_control {
    declare parameter ctx.
    declare parameter statevec.

    // This should control the trajectory based on the current mode
    // and the current state. It's outputs are the PID setpoints.
    
    print "Unimplemented".
}.

// Schedule gains based on current state (dynamic pressure, AoA)
function ctlasc_schedule_gains {
    declare parameter ctx.
    declare parameter statevec.
    
    print "Unimplemented".
}.

// Run the PID controllers given the current gains, setpoints,
// and vehicle state. Store actuator settings in context.
function ctlasc_run_pids {
    declare parameter ctx.
    declare parameter statevec.

    print "Unimplemented".
}.

// Take actuator commands (PID output) and transform it into
// actions to be taken by RCS, gimbal, control surfaces, etc.
function ctlasc_set_actuators {
    declare parameter ctx.
    declare parameter statevec.

    print "Unimplemented".
}.

