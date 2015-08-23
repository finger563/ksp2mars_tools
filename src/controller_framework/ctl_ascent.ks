// High level controller for vehicle ascent mode.
@lazyglobal off.

// Here is where constants for accessing members of the
// controller context should be defined.
global ctlascctx_logctx is 0.

// Initialize the ascent library for the vessel state vector
function ctlasc_init {
    declare parameter statevec.
    declare parameter logctx.
    
    return list(logctx).
}.

// Run the ascent control library for one iteration.
// The return value is the next controller that should be run,
// which will normally be this one until it's finished.
function ctlasc_exec {
    declare paramter statevec.
    
    // Some real cacluation should be done to update this flag.
    lock transition_to_orbit is false.
    // If ready to transition to the orbit controller, return the orbit mode flag
    if transition_to_orbit {
        return ctlmode_orbit.
    }.

    // Otherwise run the ascent controller normally.
    
    return ctlmode_ascent.
}.
