# OktaPermissionTool

## Description
This tool is used to compare the Salesforce permission sets of two profiles for comparison. The Permsisison sets can be found in the Okta Tile. The first profile is the "Mirror", which is used as a baseline set of permissions. The second Profile is the "User", which is used to compare to the Mirror.


NOTE: This tool best works if you are using Visual Studio Code to compare the permissions of users.

## How to use the tool:
   1. Start by running the OktaPermissionTool, and opening Okta to both the MIRROR and USER.
   2. On Both Profiles click on the pencil icon to edit the Salesforce Instance.
   3. Next, we will focus on one user, the MIRROR. Open the dev tools for the browser (There are a couple ways to do this, and the easiest way is to press F12 [FN+ F12]). 
   4. In the top left of this panel you should see a mouse/pointer icon surrounded a box. Click this to highlight areas of the webpage
   5. Scroll down to the Permisison Sets, and select the panel containing the individual permission set names. Press CTRL-C to copy the selected text
   6. Go to Visual Studios to the program and press ENTER. You should see a preview of the groups that have been copied.
   7. Re-peat steps 3-6 for the USER
   8. Each time that you press ENTER in the program you will copy the next missing permission set that the USER is missing from the MIRROR. 
   9. You should now be able to Paste the values into the Permission sets of the USER
