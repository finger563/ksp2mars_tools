// Library for log file output at regular intervals
@lazyglobal off.

global logctx_period is 0.  // Time period between terminal output
global logctx_lastout is 1. // Time of last terminal output

// Initialize terminal output context
function logctx_init {
    declare parameter period.

    return list(period, 0).
}.

// Function that can be called by control libraries to
// add extra data to the log file line for this time
// iteration.
function logging_add_data {
    declare parameter ctx.
    declare parameter datastring.

    // Store the string in the context somehow for later output
    
}.

// Run logging output library write phase
function logging_run {
    declare parameter ctx.
    declare parameter now.
    declare parameter dt.
    declare parameter statevec.

    if (now - ctx[logctx_lastout]) >= ctx[logctx_period] {
        // Write logging output to file, standard statevec fields first,
        // followed by extra data added by control libraries.

        // Update last print time
        set ctx[logctx_lastout] to now.
    }.
    
}.
