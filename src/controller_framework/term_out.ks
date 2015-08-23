// Library for terminal output at regular intervals
@lazyglobal off.

global termctx_period is 0.  // Time period between terminal output
global termctx_lastout is 1. // Time of last terminal output

// Initialize terminal output context
function termctx_init {
    declare parameter period.

    return list(period, 0).
}.

// Run terminal output library
function term_run {
    declare parameter ctx.
    declare parameter now.
    declare parameter dt.
    declare parameter statevec.

    if (now - ctx[termctx_lastout]) >= ctx[termctx_period] {
        // Print terminal output
        print "Test print, dt is: " + dt.

        // Update last print time
        set ctx[termctx_lastout] to now.
    }.
    
}.
