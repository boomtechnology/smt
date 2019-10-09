DISPLAY=":0"
LINT_INCLUDE="src/boom/cad/cadboom src/boom/cad/engine"
LINUX="NO"
MKBOOM_DIR=""

echo "$OSTYPE" | grep "linux" >/dev/null && LINUX="YES"

# Overridden Functions #################################################################################################

function command-lint {
    # do nothing. To be restored when we re-convert this container for doing development work.
    eval ""
}

function execute-test-run {
    echo "Starting test run $TEST_RUN at $(date):"

    $VIRTUAL_BIN/testflo || return 1

    return 0
}
