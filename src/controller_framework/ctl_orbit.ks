// High level controller for vehicle orbit mode.
@lazyglobal off.

// Here is where constants for accessing members of the
// controller context should be defined.
global ctlobtctx_logctx is 0.

// Initialize the orbit library for the vessel state vector
function ctlobt_init {
    declare parameter statevec.
    declare parameter logctx.
    
    return list(logctx).
}.

// Run the orbit control library for one iteration.
// The return value is the next controller that should be run,
// which will normally be this one until it's finished.
function ctlobt_exec {
    declare paramter statevec.
    
    // Some real cacluation should be done to update this flag.
    lock transition_to_land is false.
    // If ready to transition to the landing controller, return the landing mode flag
    if transition_to_land {
        return ctlmode_landing.
    }.

    // Otherwise run the orbit controller normally.
    
    return ctlmode_orbit.
}.
