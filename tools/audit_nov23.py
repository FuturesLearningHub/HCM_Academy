# Assignment change review notes, Nov 23, 2026 (HCM_Academy_Audit_Notes.docx).
# Covers Change Assignment, Add Assignment, and Change Working Hours. The pre-assessment edits from the same
# notes are in assets/assessments.js.
# What the notes state as fact is applied here. What they ask to confirm is an open item ("Open item: ...")
# and is not guessed. apply(COURSES) runs last in tools/course_content.py, after the merges in restructure.py.
# Rules: no em or en dashes; no individual names.

AUDIT_ON = "Nov 23, 2026"
NOTES = {}   # slug: what changed, shown in the course record and on the What changed page
O = {}       # slug: fields to replace

def s(t, d="", sub=None):
    x = {"t": t, "d": d}
    if sub: x["sub"] = sub
    return x

def q(text, options, answer, why):
    return {"q": text, "o": options, "a": answer, "why": why}

OVERRIDE_D = ("Position Override toggles decide where a field's value comes from. On (blue): the assignment synchronizes with the "
              "position. Off (gray): the assignment keeps the value it has now. This applies to fields such as Location, Working Hours, "
              "and Manager Name.")
OVERRIDE_SUB = ["On (blue): take the value from the position", "Off (gray): keep the assignment's current value"]
MANAGER_D = ("The manager on the position may not be the employee's actual manager. Check who the employee really reports to before "
             "you let the position's Manager Name replace the value on the assignment.")
TRACK_D = ("Review the transaction and Submit. Then open Created by Me on the Oracle home screen: it lists the transactions you "
           "submitted and shows where each one is in approval.")
REQUIRED_FIELDS = ("Open item: confirm the full list of assignment fields HCMs must maintain, such as work-from-home status, manager "
                   "status, remote or hybrid work, working with minors, and driving for the university. Until it is confirmed, ask HRIS "
                   "rather than deciding which fields are required.")

# ───────────── Change Assignment ─────────────
O["change-assignment"] = dict(
    time="8 min",
    intro=["Change Assignment is the transaction for broader changes to an employee's current assignment, or for several changes in one "
           "transaction. Examples: ACA eligibility, default expense account, leave status, the primary indicator, or an update that "
           "touches several fields or sections.",
           "For a single change, use the direct action when one is available: Change Manager, Change Location, Direct Reports, or "
           "Change Working Hours. Start from Employment Info so you can review the record before you change it."],
    use_when="An employee's assignment needs a broader update, or several changes in one transaction. For one change that has a direct action, use that action instead.",
    steps=[
        s("Open the employee's Employment Info.",
          "Our Workforce > Employment Info, then search for the employee. Review the current assignment, job, position, location, FTE, "
          "headcount, and default expense account before you change anything. Employment Info is the recommended starting point, but it "
          "is not the only way to start a transaction."),
        s("Pick a direct action or Change Assignment.",
          "From Employment Info, use the three-dot menu for a single direct action. Use Change Assignment for broader changes or when "
          "several fields need to change.",
          ["One change with a direct action (Change Manager, Change Location, Direct Reports, Change Working Hours): the three-dot menu",
           "Broader changes, or several fields at once: Change Assignment"]),
        s("Select the sections this transaction needs, then Continue.",
          "Add only the sections the change touches. Use Comments and Attachments when HRIS needs supporting documentation or an "
          "explanation to review or approve the change.",
          ["Manager", "Salary", "Direct Reports", "Payroll Details", "Compensation", "Comments and Attachments"]),
        s("Enter the effective date.",
          "The effective date is the date the change takes effect on the assignment. The payroll cutoff is a separate date: it decides "
          "which payroll can process the change. If Oracle warns about a future-dated change, check the record's history; it may be "
          "another HCM's transaction."),
        s("Choose the type of change, then the action reason.",
          "Change Assignment is the whole transaction. Assignment Change is one type of change inside it; others include ACA "
          "Eligibility, Default Expense Account, Leave Status, and Primary Indicator. After Assignment Change, pick the action reason, "
          "such as Position Change Within a Business Unit. Leave Status is its own type of change with its own action reasons; it is "
          "not a reason under Assignment Change."),
        s("Check the Position Override toggles.", OVERRIDE_D, OVERRIDE_SUB),
        s("Verify the manager before the position overrides it.", MANAGER_D),
        s("Update the fields that are changing, including the Business Title.",
          "Change only the fields that aren't grayed out. Business Title is the department's working title and can be updated on the "
          "assignment. See Titles in Oracle below."),
        s("Fill in the required assignment information.",
          "Keep the assignment attributes current, such as work-from-home status, manager status, remote or hybrid work, working with "
          "minors, and driving for the university."),
        s("After a reclassification, check the fields the position may not update.",
          "After a position reclassification, some assignment fields may need a manual update, for example person type, location, "
          "working hours, and hourly salary."),
        s("Review, submit, and track approval.", TRACK_D + " Some direct actions, such as Change Manager, may not go through approval."),
    ],
    table=dict(title="Titles in Oracle", head=["Title", "What it is"], rows=[
        ["Position Title", "The name given to the position"],
        ["Job Title", "The Job Architecture (job code) title tied to the position"],
        ["Business Title", "The department's working title. You can update it on the assignment."]]),
    watch=["Change Assignment is the whole transaction; Assignment Change is one type of change inside it. Leave Status is a separate "
           "type with its own action reasons, so don't look for it under Assignment Change.",
           "Don't let a position override replace the employee's real manager. Check Manager Name before you leave its toggle on.",
           "One employee can have three different titles: Position, Job, and Business.",
           "Open item: confirm whether moving an employee to another position in the same business unit uses Assignment Change (reason "
           "Position Change Within a Business Unit) or Transfer. The course and knowledge check will be updated once it is confirmed.",
           "Open item: confirm which sections (Manager, Salary, Direct Reports, Payroll Details, Compensation, Comments and Attachments) "
           "are required, optional, or conditional for each type of change.",
           REQUIRED_FIELDS,
           "Open item: confirm how the effective date, the payroll cutoff, and payroll processing relate when a change is entered after "
           "the monthly (exempt) cutoff. Missing the cutoff should not be read as changing the effective date.",
           "Open item: confirm which fields must be updated by hand on the assignment after a position reclassification.",
           "Open item: confirm what belongs in Official Documentation, when to use it, whether it is required, and how it differs from "
           "Comments and Attachments.",
           "Open item: confirm which assignment transactions need approval and which do not (for example, Change Manager)."],
    quiz=[q("Where do you typically start an assignment change?",
            ["Our Workforce > Employment Info", "Workforce Structures > Positions", "Individual Compensation"], 0,
            "Employment Info is the recommended starting point because it shows the current record first. It is not the only way to start."),
          q("What is the difference between Change Assignment and Assignment Change?",
            ["They are two names for the same thing",
             "Change Assignment is the whole transaction; Assignment Change is one type of change inside it",
             "Assignment Change is only for managers"], 1,
            "Change Assignment is the transaction. Assignment Change is one of the types of change you can pick inside it."),
          q("The Position Override toggle for Manager Name is on (blue). What happens?",
            ["The assignment keeps its current manager", "The assignment takes the manager from the position", "Oracle asks the employee"], 1,
            "On synchronizes the field from the position, so first check that the position's manager is the employee's real manager.")],
)
NOTES["change-assignment"] = ("From the assignment change review: when to use Change Assignment or a direct action; Change Assignment and "
    "Assignment Change told apart; sections, effective date and cutoff, Position Overrides and Manager Name, and the three titles "
    "explained; tracking in Created by Me. Whether a move within the business unit is a transfer is now an open item, and the knowledge "
    "check no longer tests it.")

# ───────────── Change Working Hours ─────────────
O["change-working-hours"] = dict(
    time="6 min",
    intro=["Changing working hours changes FTE, and it can also affect salary, benefits, and PTO.",
           "The process depends on the employee. A non-exempt (hourly) employee's hourly rate generally doesn't change just because the "
           "hours change. For an exempt (salaried) employee, an FTE change may also need a salary change. So there are two ways to do it: "
           "working hours only, or working hours and salary together."],
    use_when="An employee's scheduled hours or FTE change.",
    steps_title="Two scenarios: hours only, or hours and salary",
    steps=[
        s("Decide which scenario you're in.",
          "If only the hours or FTE change and pay stays as it is, it's working hours only. If the salary also has to change, it's "
          "working hours and salary.",
          ["Working hours only: Change Working Hours", "Working hours and salary: Change Assignment with Salary"]),
        s("Working hours only: open Employment Info, then the three-dot menu.",
          "Go to Our Workforce > Employment Information and search for the employee. Select the three-dot menu, then Change Working Hours."),
        s("Working hours only: enter the effective date and the new hours, then submit.",
          "Enter the new weekly hours (for example, 30). Standard working hours stay at 40, so FTE recalculates (30 of 40 = 0.75)."),
        s("Working hours and salary: open Employment Info and choose Change Assignment.",
          "Go to Our Workforce > Employment Information and search for the employee. Select Change Assignment, then the Salary and "
          "Comments and Attachments sections. Add Payroll Details if it's needed, for example when the employee changes from exempt to "
          "non-exempt. Continue."),
        s("Working hours and salary: enter the effective date, then Assignment Change and the action reason.",
          "Working Hours Change doesn't appear as a reason in this path. Ask HRIS which reason to use until the course names it."),
        s("Working hours and salary: change the hours, then the salary.",
          "Enter the new weekly hours; FTE recalculates. Oracle prorates the salary to the new FTE. If the agreed salary is different, "
          "enter the agreed amount."),
        s("Working hours and salary: add comments and documents, then submit.",
          "Say what is changing and why, and attach the approval or agreement before you submit. Track it from Created by Me on the "
          "Oracle home screen."),
    ],
    table=dict(title="Exempt or non-exempt", head=["", "Exempt (salaried)", "Non-exempt (hourly)"], rows=[
        ["Pay is based on", "A salary for the FTE", "An hourly rate for hours worked"],
        ["When hours change", "The salary may need to change too", "The hourly rate generally stays the same"],
        ["Usual path", "Change Assignment with Salary, when the salary changes", "Change Working Hours"],
        ["Moving between exempt and non-exempt", "Include Payroll Details", "Include Payroll Details"]]),
    watch=["Change Salary with the reason Change in working hours changes only the salary. The hours need their own transaction, so when "
           "both change, use Change Assignment with Salary.",
           "An FTE change can affect benefits and PTO, not only pay.",
           "Open item: confirm that Change Assignment is the right process when both working hours (FTE) and salary change.",
           "Open item: confirm the action reason for a combined working hours and salary change.",
           "Open item: confirm when an exempt employee's salary should change because their FTE changes, and when an hours change needs "
           "no salary or hourly rate change.",
           "Open item: confirm when Payroll Details must be included, and any other differences between exempt and non-exempt employees.",
           "Open item: confirm the benefits and PTO impacts of an FTE change to explain in this course."],
    quiz=[q("Full-time 40 hours goes to 30. What's the FTE?", ["1", "0.75", "0.5"], 1, "30 of a 40-hour standard week is 0.75."),
          q("A non-exempt (hourly) employee drops from 40 to 30 hours, and the hourly rate stays the same. Which action?",
            ["Change Working Hours from the three-dot menu", "Change Assignment with Salary", "Change Salary"], 0,
            "Only the hours change, and hourly rates generally don't change with hours."),
          q("An employee's hours and salary both change. What do you use?",
            ["Change Working Hours now and Change Salary later",
             "Change Assignment, with Salary and Comments and Attachments selected",
             "Change Salary with the reason Change in working hours"], 1,
            "Change Assignment with Salary changes both in one transaction, with the reason documented.")],
)
NOTES["change-working-hours"] = ("From the assignment change review: split into two scenarios, working hours only (Change Working Hours) "
    "and working hours and salary (Change Assignment); exempt and non-exempt explained; no longer says to pick any reason that fits. "
    "The action reason, salary rules, and benefits and PTO impacts are open items.")

# ───────────── Add Assignment ─────────────
def _add_assignment(c):
    pick = c["steps"][:4]   # Add a Work Relationship or add an Assignment? (unchanged)
    c.update(
        time="10 min",
        intro=["Add Assignment is used mainly for students, who often hold more than one job. Most staff have only one assignment, so "
               "Add Assignment is not a standard staff transaction.",
               "In Oracle, a person has one person record, one or more work relationships, and one or more assignments inside each work "
               "relationship. The record the student already has tells you whether to add an assignment or a work relationship."],
        use_when="A student already in Oracle is taking on another job, or you are setting up paid work for a student.",
        steps=pick + [
            s("Confirm the position for the new job is active.",
              "The added assignment must point to an active position. Do not reactivate an inactive position or reuse one built for a "
              "different worker type."),
            s("Open the student's Employment Info and find an active assignment.",
              "Our Workforce > Employment Info, search for the student, and review the assignments they have."),
            s("From that assignment's three-dot menu, select Add Assignment.",
              "Starting from Employment Info is the recommended path."),
            s("Select the sections to include.", "Then Continue.",
              ["Payroll Details: include", "Salary: include", "Compensation: not needed",
               "Direct Reports: only if the person will have direct reports"]),
            s("Enter the start date, and whether the assignment is temporary or permanent.",
              "The start date is the first day of the new job."),
            s("Select Add Assignment, then the action reason.",
              "Ask HRIS which action reason to use until the course names it; don't pick one just because it's on the list."),
            s("Select the business unit and the active position.",
              "Fields such as job and department default from the position. Check the working hours for the new assignment."),
            s("Check the Position Override toggles, especially Manager Name.", OVERRIDE_D + " " + MANAGER_D, OVERRIDE_SUB),
            s("Enter the required assignment information.",
              "Fill in each required field for the new assignment. If you're not sure a field is required, ask HRIS."),
            s("Know what the primary flag means before you touch it.",
              "A person has one primary assignment: the one Oracle treats as their main job. A new assignment is not primary by default. "
              "Leave the existing job as primary unless the new job is now the person's main job.",
              ["Only one assignment can be primary"]),
            s("Review, submit, and track approval.", TRACK_D),
            s("After approval, check the new assignment in Employment Info.",
              "Return to Employment Info, open the new assignment, and confirm its details are right."),
            s("Add costing if this job shouldn't use the default.",
              "Each assignment has its own costing. Blank costing means the work unit default applies. If this job should charge a "
              "different account, add costing for it."),
        ],
        watch=[w for w in c["watch"] if w.startswith("Adding a Work Relationship")] + [
            "Don't treat Add Assignment as a standard staff transaction. Most staff have only one assignment.",
            "Don't let a position override replace the student's real manager. Check Manager Name before you leave its toggle on.",
            "Each assignment has its own costing, hours, and pay.",
            "Open item: confirm whether student assignments use six-digit job codes.",
            "Open item: confirm how Add Assignment applies to faculty.",
            "Open item: confirm which action reasons to use for an added assignment.",
            "Open item: confirm whether adding a second assignment needs approval.",
            "Open item: confirm which assignment fields are mandatory.",
            "Open item: confirm the rules for the primary flag: when to change it, which assignment should be primary, and what it affects.",
            "Open item: confirm when an added assignment needs its own costing.",
            "Open item: confirm whether starting from Employment Info is required or only recommended, and the exact Quick Action names."],
        quiz=[x for x in c["quiz"][:2]] + [
            q("You're adding an assignment for a student's second job. Which sections do you include?",
              ["Payroll Details and Salary", "Compensation and Direct Reports, always", "No sections"], 0,
              "Include Payroll Details and Salary. Compensation isn't needed, and Direct Reports only if the person will manage people."),
            q("The new job is a small side role. What do you do with the primary flag?",
              ["Leave the existing job as primary", "Make the new job primary", "Mark both as primary"], 0,
              "Only one assignment can be primary, and it should be the person's main job."),
            q("Where do you enter the salary for the new job?",
              ["On the existing assignment, as a raise", "In UKG", "On the new assignment's Salary section"], 2,
              "Each assignment carries its own pay, so the new job's salary goes on the new assignment.")],
    )
NOTES["add-assignment"] = ("From the assignment change review: Add Assignment is presented as mainly for students; starts from the "
    "three-dot menu in Employment Info; sections, Position Overrides, the primary flag, tracking in Created by Me, checking after approval, "
    "and costing added. Job codes, faculty, action reasons, approval, mandatory fields, and primary flag rules are open items.")

def apply(courses):
    by = {c["slug"]: c for c in courses}
    for slug, fields in O.items():
        by[slug].update(fields)
    _add_assignment(by["add-assignment"])
    return courses
