// Main driver file for vessel control system
@lazyglobal off.

// Import control mode "enumeration"
run ctlmodes.

// Import the state vector library
run statevec.

// Import the terminal output/logging library
run term_out.
run logging_out.

// Load control libraries for the three highest level states
run ctl_idle.
run ctl_ascent.
run ctl_orbital.
run ctl_landing.

// Initialize the craft state vector
global statevec is statevec_init().

// Initialize terminal log context (passing the print period in seconds)
global termctx is termctx_init(1.0).
// Initialize the logfile context (passing the filename and print period in seconds)
global logctx is logctx_init("VesselName.csv", 0.1).

// Initialize us in idle mode.
global ctlmode is ctlmode_idle.
global ctlmode_ctx is ctlidle_init(statevec, logctx).
global newmode is ctlmode_idle.

// Flag will be set to true on state change for initialization of new state
global state_change is false.
// Flag which will shutdown the entire controller.
global haltflag is false.

// Main loop timing control and measurement variables
global main_iter_t0 is TIME:SECONDS.
global main_start_time is iter_t0.
global main_now is 0.
global main_dt is 0.

// Wait a touch so our first dt isn't 0 (which could cause problems)
wait 0.1.

until haltflag {
    // Update timing variables
    set main_now to TIME:SECONDS.
    set main_dt to main_now - main_t0.
    set main_t0 to main_now.

    // Update the vehicle state vector once per iteration
    // (so expensive state caclulations are only done once).
    statevec_update(statevec).
    
    // Run the highest level state machine
    if ctlmode = ctlmode_idle {
        // Check if we just moved to this state
        if state_change {
            // Initalize the new control library for the new state
            set ctlmode_ctx to ctlidl_init(statevec, logctx).
            // Mark state as updated
            set state_change to false.
        }.

        set newmode to ctlidl_exec(statevec).
    }
    else if ctlmode = ctlmode_ascent {
        // Check if we just moved to this state
        if state_change {
            // Initalize the new control library for the new state
            set ctlmode_ctx to ctlasc_init(statevec, logctx).
            // Mark state as updated
            set state_change to false.
        }.

        set newmode to ctlasc_exec(statevec).
    }
    else if ctlmode = ctlmode_orbit {
        // Check if we just moved to this state
        if state_change {
            // Initalize the new control library for the new state
            set ctlmode_ctx to ctlobt_init(statevec, logctx).
            // Mark state as updated
            set state_change to false.
        }.

        set newmode to ctlobt_exec(statevec).
    }
    else if ctlmode = ctlmode_land {
        // Check if we just moved to this state
        if state_change {
            // Initalize the new control library for the new state
            set ctlmode_ctx to ctllnd_init(statevec, logctx).
            // Mark state as updated
            set state_change to false.
        }.

        set newmode to ctllnd_exec(statevec).
    }.

    // Check if we've moved to a new state.
    if newmode <> ctlmode {
        state_change to true.
    }.

    // Run the terminal ouput library
    term_run(termctx, main_now, main_dt, statevec).
    // Run the logfile output library
    logging_run(logctx, main_now, main_dt, statevec).

    // Wait the shortest time possible (1 physics frame). Cut this out if performance requires.
    wait 0.001.
}.

