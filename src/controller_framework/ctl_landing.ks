// High level controller for vehicle landing mode.
@lazyglobal off.

// Here is where constants for accessing members of the
// controller context should be defined.
global ctllndctx_logctx is 0.

// Initialize the landing library for the vessel state vector
function ctllnd_init {
    declare parameter statevec.
    declare parameter logctx.
    
    return list(logctx).
}.

// Run the landing control library for one iteration.
// The return value is the next controller that should be run,
// which will normally be this one until it's finished.
function ctllnd_exec {
    declare paramter statevec.
    
    // Some real cacluation should be done to update this flag.
    lock transition_to_idle is false.
    // If ready to transition to the idle controller, return the idle mode flag
    if transition_to_idle {
        return ctlmode_idle.
    }.

    // Otherwise run the landing controller normally.
    
    return ctlmode_landing.
}.
