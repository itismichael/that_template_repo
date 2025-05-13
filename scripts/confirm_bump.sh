#!/bin/sh
# Helper script to preview a Commitizen version bump and ask for confirmation before applying.
# Usage: ./confirm_bump.sh /path/to/commitizen_executable

COMMITIZEN_EXEC="$1"

if [ -z "$COMMITIZEN_EXEC" ]; then
  echo "Error: Commitizen executable path not provided to confirm_bump.sh." >&2
  exit 1
fi

set -e # Exit immediately if a command exits with a non-zero status.

echo "Running Commitizen bump (dry-run)..."
# The output of dry-run will go to stdout/stderr for the user to see.
"$COMMITIZEN_EXEC" bump --dry-run

echo # Add a blank line for better readability before the prompt

# Ask for confirmation
# Using printf for better portability and control over newline
printf "Apply these version bump changes? (y/N): "
# Using 'head -n 1' to read a single line of input for better compatibility across shells
# Read directly from TTY for interactive tasks when 'task' uses -i or the task is interactive
read -r confirmation < /dev/tty 
echo # Newline after user input for cleaner subsequent output

if [ "$confirmation" = "y" ] || [ "$confirmation" = "Y" ]; then
  echo "Applying version bump..."
  "$COMMITIZEN_EXEC" bump
  echo "Version bump applied successfully!"
  echo "Remember to push the changes and tags using 'task release:push'."
else
  echo "Version bump aborted by user."
  # Exiting with 0 so 'task' doesn't mark this as a failure if user intentionally aborts.
  exit 0
fi
