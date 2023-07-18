# Online-Banking-System-Back-End

## User Authentication:

SignupView: This allows a new user to sign up. It involves taking a username, password, email, and names, then creating a new user in the database.
LoginView: Allows users to log into their account by verifying their credentials.
profile_view: Allows a logged-in user to view their profile information including their username, email, and names.
profile_edit_view: Allows a logged-in user to edit their profile information including their email and names. They can also update their password.
logout_view: Logs out the current user, removing their session data.

## Bank Management:

AddBankView: This allows a logged-in user to add a new bank. The user provides the bank's name, description, institution number, and SWIFT code.
DisplayBankView: Allows users to view a list of all banks.
DisplayDetailBankView: Allows users to view the details of a specific bank.

## Branch Management:

AddBranchView: This allows a logged-in user to add a new branch to a bank they own. The user provides the branch's name, transit number, address, and capacity.
DisplayAllBranchesView: Allows users to view all branches of a specific bank.
DisplaySpecificBranchView: Allows users to view the details of a specific branch.

All views check if the user is authenticated before allowing access to the respective functionality. If the user is not authenticated, an 'UNAUTHORIZED' message is returned with status 401.

For 'AddBranchView', there is an additional check to ensure that the user owns the bank they are trying to add a branch to. If the user is not the owner of the bank, a 'FORBIDDEN' message is returned with status 403.

Finally, the project leverages Django's powerful forms for user inputs, handling validations and data cleaning to ensure the data integrity and security. Forms include SignupForm, LoginForm, UpdateUserForm, AddBankForm, and AddBranchForm.

Each form performs necessary checks and raises appropriate error messages when a field is missing or invalid. For instance, 'SignupForm' and 'UpdateUserForm' check if the two password fields match and if the email is valid.

Please remember that this project is a starting point. Real-world applications may require further enhancements such as more robust error handling, permissions and roles handling, data pagination, API endpoints, etc.
