1) A business object like "Article" or "Transaction" - Done

2) There must be at least one Transaction object in the database. Fixtures are okay, or use the admin interface to manually create example objects. - Done

3) Staff admin users which have restricted privileges. These are not django-admin superusers. That is, they have some read/write restrictions. Make at least 3 separate staff admin users. - Done

4) In django-admin, the staff admin users should be shown a button or link (custom admin action) that says "Review" which takes the user to another page where they can choose "Authorize", "Reject", or "Flag". This should be specific to an object that the admin has selected. - working

5) Once 2 of the 3 users have clicked "Authorize", some action should be taken, such as printing a message to the logs or some other indication that the action has occurred.

6) If one of the users has "Rejected" or "Flagged" the item, then 2-of-3 approval should not trigger the action.

The purpose of this feature is to allow staff members to "approve" or "reject" some object. Group approval allows an action to take place, and rejection prevents the action from moving forward. Note that this is not "voting"--- it is only a threshold.