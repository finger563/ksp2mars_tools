// High level controller for vehicle idle mode.
@lazyglobal off.

// Idle controller context member constants
global ctlidlctx_logctx is 0.

// Initialize the idle library for the vessel state vector
function ctlidl_init {
    declare parameter statevec.
    declare parameter logctx.
    
    return list(logctx).
}.

// Run the idle control library for one iteration.
// The return value is the next controller that should be run,
// which will normally be this one until it's finished.
function ctlidl_exec {
    declare paramter statevec.
    
    // Some real cacluation should be done to update this flag.
    lock transition_to_ascent is false.
    // If ready to transition to the ascent controller, return the ascent mode flag
    if transition_to_ascent {
        return ctlmode_ascent.
    }.

    // Otherwise run the idle controller normally.
    
    return ctlmode_idle.
}.
