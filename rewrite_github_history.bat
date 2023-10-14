@echo off

:: Set your main email address

set main_email=YOUR_MAIN_EMAIL_ID
git config --global user.name NAME
git config --global user.email YOUR_MAIN_EMAIL_ID

:: Define the email addresses to be rewritten
set other_emails=OTHER_EMAIL_ID_1 OTHER_EMAIL_ID_2


:: Rewrite the commit history for commits with different email addresses
for %%i in (%other_emails%) do (
    git filter-branch --env-filter "
    if [ \"\$GIT_COMMITTER_EMAIL\" == '%%i' ]; then
        export GIT_COMMITTER_NAME=\"\$GIT_COMMITTER_NAME\"
        export GIT_COMMITTER_EMAIL=\"%main_email%\"
    fi
    if [ \"\$GIT_AUTHOR_EMAIL\" == '%%i' ]; then
        export GIT_AUTHOR_NAME=\"\$GIT_AUTHOR_NAME\"
        export GIT_AUTHOR_EMAIL=\"%main_email%\"
    fi
    " -- --all
)

:: Remove the backup references created by filter-branch
for /f %%r in ('git for-each-ref --format="%(refname)" refs/original/') do git update-ref -d %%r

:: Force push the changes to your remote repository
git push origin main --force 

:: Cleanup temporary files
rmdir /s /q .git\refs\original
rmdir /s /q .git\logs

:: Inform the user that the script has finished
echo Git history has been rewritten with the main email address for specified commits.

:: Pause to keep the terminal open
pause
