# Vanderbilt SME review, November 2026 (from the section audit workbook).
# What reviewers stated as fact is applied here; what they asked is an open item. Reviewers are not named.
# apply(COURSES) runs after the course data is assembled (see course_content.py). It replaces the reviewed
# fields of each course, merges, splits, and moves courses as the reviewers recommended, and records a
# change note for each course in NOTES (shown in the course record and on the What changed page).
REVIEWED = "Reviewed by a Vanderbilt SME in November 2026, and the review's changes are in. Confirm the open items before release."
NOTES = {}        # slug: what changed, for the course record
VERIFY = {}       # slug: screen checks that replace the old list
REMOVED = {}      # slug: the course it was merged into
O = {}            # slug: fields to replace

def s(t, d="", sub=None):
    x = {"t": t, "d": d}
    if sub: x["sub"] = sub
    return x

def q(text, options, answer, why):
    return {"q": text, "o": options, "a": answer, "why": why}

# ───────────── 00 Start Here ─────────────
O["hcm-structure"] = dict(
    intro=["Oracle HCM stores every person inside a set of structures: who legally employs them, which business unit and work unit they belong to, what job and position they hold, and how they are paid.",
           "Knowing these terms makes every other course easier, because each transaction you submit changes one or more of them."],
    use_when="You are new to Oracle HCM, or a screen uses a term (legal employer, work relationship, work unit, assignment) you are not sure about.",
    steps=[
        s("Start at the top: the enterprise and the legal employer.", "The enterprise is Vanderbilt as a whole in Oracle. The legal employer is the organization that is legally the employer: it hires the person, pays them, and reports their taxes. Every work relationship belongs to one legal employer."),
        s("Know the difference between a business unit and a work unit.", "A business unit (BU) is a large part of Vanderbilt that does its own HR and finance processing. A work unit is a smaller group inside a business unit, where people are organized and, by default, costed.",
          ["Use Work Unit, the term Oracle uses, rather than department.", "Some departments are grouped into a single work unit."]),
        s("Know what a work relationship is.", "A work relationship is the link between a person and a legal employer, for example as an employee, a contingent worker, or a nonworker. A person can have more than one, and each work relationship holds one or more assignments."),
        s("Tell a job from a position.", "A job is a generic role (for example, Administrative Assistant). A position is one specific instance of a job in a specific work unit, with its own budgeted details. People are hired into positions, and the assignment can inherit values from the position.",
          ["Job codes come from Vanderbilt's job architecture. Not every worker type has a six-digit job code yet."]),
        s("Understand the grade.", "A grade sets the pay range attached to a job or position. It does not set a person's actual salary, which is recorded separately on the assignment."),
        s("Read the assignment.", "The assignment is where the job, position, work unit, location, manager, hours, and payroll live.", ["A person has only one primary work relationship and one primary assignment in it."]),
        s("Use the person number.", "Every person in Oracle has a unique person number. Use it to search, and to tell apart people with similar names."),
        s("Check the person type before you act.", "Person types (such as Employee, Contingent Worker, Nonworker, Pending Worker) tell Oracle and payroll how to treat the record. Picking the wrong one changes pay, benefits, and reporting."),
    ],
    table=dict(title="Terms at a glance", head=["Term", "What it means for you"], rows=[
        ["Legal employer", "The organization that hires, pays, and reports taxes for the person"],
        ["Business unit", "A large part of Vanderbilt that does its own HR and finance processing"],
        ["Work unit", "A group inside a business unit where people sit and are costed by default"],
        ["Work relationship", "The person's link to a legal employer, such as employee or nonworker"],
        ["Job vs. position", "Generic role vs. a specific seat in a work unit"],
        ["Assignment", "Where job, pay, hours, and manager live"],
        ["Person number", "The unique number that identifies a person"]]),
    watch=["Changes to a position can flow into every incumbent's assignment. Know which fields the position controls before you edit a position.",
           "Do not reuse or repurpose a position for a different worker type; ask Compensation instead.",
           "Open item: confirm whether HCM access is scoped to the business unit or the work unit.",
           "Open item: confirm which person types and work relationship types Vanderbilt uses and what each one means for pay."],
    docs=[],
    quiz=[q("Where in Oracle do a person's job, work unit, manager, and payroll live?", ["On the person record", "On the assignment", "On the grade"], 1, "The assignment, inside a work relationship, holds the job, position, work unit, manager, hours, and payroll."),
          q("What is the difference between a business unit and a work unit?", ["A work unit is a group inside a business unit", "They are the same thing", "A business unit is inside a work unit"], 0, "A business unit is a large part of Vanderbilt; work units sit inside it, and people are costed to the work unit by default."),
          q("What is the safest way to tell apart two people with similar names?", ["Their department", "Their person number", "Their first name"], 1, "Every person has a unique person number.")])
NOTES["hcm-structure"] = "From the SME review: clearer definitions of legal employer, business unit, and work unit (the Oracle term); work relationship and person number added; a watch-out corrected; links meant for system administrators removed."

O["workflow-worklists"] = dict(
    intro=["Most transactions you submit in Oracle HCM do not take effect right away. They route to approvers, and each approver sees a task in their notifications or worklist.",
           "Know where to look, and what Withdraw and Send Back do. That keeps transactions from stalling before the payroll cutoff."],
    watch=["Check the bell daily, and before every payroll cutoff. A transaction waiting on an approver is not in payroll yet.",
           "Rejecting means the whole approval chain starts over after resubmission; send back or request information when a small fix is all that is needed.",
           "If people or transactions in your area are missing, your access may need an area of responsibility. Your business unit approver requests it.",
           "Open item: confirm Vanderbilt's approval chains by transaction type, whether delegation is enabled for HCMs, and the exact action labels on screen."],
    docs=[])
NOTES["workflow-worklists"] = "From the SME review: clearer wording, a note on areas of responsibility for HCM access, and links meant for system administrators removed."

O["quick-actions-person-info"] = dict(docs=[])
NOTES["quick-actions-person-info"] = "From the SME review: documentation links that did not help HCMs removed."

O["ferpa-for-staff"] = dict(steps_patch={0: s("Know what an education record is.",
    "Education records are records directly related to a student and maintained by the school, such as transcripts, class schedules, grades, and disciplinary records. Those live in YES, Vanderbilt's student system, not in Oracle. What you do see in Oracle when you hire and pay student workers, such as Federal Work-Study (FWS) status and personal information, needs the same care.",
    ["Something you only observed in person is generally not a record."])})
NOTES["ferpa-for-staff"] = "From the SME review: a clearer definition of an education record, and what HCMs actually see in Oracle (such as FWS status) versus what lives in YES."

O["i9-background-by-worker-type"] = dict(steps_insert={1: s("Know who counts as each worker type.",
    "Interns can be Vanderbilt students or people with no other tie to Vanderbilt, including students at other schools. Only Vanderbilt students hold a student relationship; other interns are set up as postdocs, temporary staff, or term staff, depending on the payroll relationship. Campus affiliates can be independent contractors, employees of contracted vendors, or non-compensated affiliates.")},
    watch_add=["Open item: confirm whether every type of campus affiliate needs an Oracle record.",
               "Open item: add when and how to complete the Formstack background check request."])
NOTES["i9-background-by-worker-type"] = "From the SME review: who counts as an intern and as a campus affiliate, and open items on Oracle records for affiliates and the Formstack request."

O["employee-vs-contractor"] = dict(steps_insert={5: s("Use the IC20 test for professional services agreements.",
    "When someone requests a professional services agreement (PSA), Finance typically shares the IC20 test. The completed test goes to an engagement consultant, who advises on the classification. Fill it out with the requestor so the answers are accurate.",
    ["Some divisions have the HCM complete the IC20 with the requestor."])},
    watch_replace={2: "Open item: confirm whether HCMs in every area complete the IC20 with the requestor."})
NOTES["employee-vs-contractor"] = "From the SME review: the IC20 test and the engagement consultant's review for professional services agreements."

O["data-integrity"] = dict(steps_patch={
    2: s("Check dates as carefully as values.", "Oracle records are date effective. Every transaction that affects pay needs the right effective date: the date the change takes effect for pay. That includes hires, salary changes, working hours changes, transfers, terminations, one-time payments, and costing changes. A wrong date can pay someone too early or too late, or create retro pay.",
         ["An update adds history; a correction overwrites the old value with no history."]),
    3: s("Remember costing follows the data.", "Pay is charged to the costing on the assignment. Left blank, it uses the work unit's default costing, so a wrong work unit means pay is charged to the wrong place. A mistyped costing string does not default: it goes to suspense. When someone transfers to a new business unit, the HCM in the new area reviews and updates their costing."),
    5: s("Review before you submit.", "Read every field back against the source document, then check the costing reports before the payroll cutoff. The Cost Allocation Verification Report flags mismatched data.", ["Check: person, effective date, position, hours, pay, costing."])},
    watch_add=["Open item: add a walkthrough of the Departmental Playbook costing report."])
NOTES["data-integrity"] = "From the SME review: which transactions need an effective date, what costing follows (including suspense), and the Cost Allocation Verification Report."


# ───────────── 01 Positions, Recruitment & Hiring ─────────────
NEW = {}          # slug: (after slug, course) for courses the review adds

O["job-architecture"] = dict(
    name="Job Architecture overview, Part 1: How talent is organized and how it impacts recruiting decisions",
    title_pre="Job architecture,", title_em="part 1",
    intro=["Job architecture is a basic HR framework: it groups an organization's jobs by the kind of work and the level of the work, so similar jobs are titled, leveled, and paid consistently.",
           "Learn the terms first. Part 2 shows how Vanderbilt's job architecture is set up in Oracle."],
    use_when="You are new to job architecture, or you need to read a job title, family, or level before you build a position or requisition.",
    steps_title="Key terms",
    steps=[
        s("Job architecture", "The framework that organizes every job by the kind of work and the level of the work. Vanderbilt moved its staff jobs into a job architecture."),
        s("Job family and sub-family", "A job family groups jobs that do a similar kind of work. A sub-family is a narrower group inside a family."),
        s("Growth stream", "The career track a job sits in. Jobs in the same growth stream grow in scope as their level goes up."),
        s("Job level", "A job's level within its growth stream, set by the scope of its duties. The job name ends with it, such as Accountant Support SS2."),
        s("Compensation matches the role to a job.", "Compensation compares the role's duties to the job architecture and gives you the job on the pre-search memo."),
        s("Review the positions in your area.", "Look at the positions in your assigned area and how they fit in the job architecture. An employee roster report or workforce position report shows each person's job code, job name, and position name."),
    ],
    watch=["Review the positions in your assigned area and how they fit in the job architecture before you build or post anything.",
           "Ask Compensation or your engagement consultant for the materials that show Vanderbilt's families, growth streams, and levels.",
           "Open item: add links to Vanderbilt's job architecture resources and to the employee roster and workforce position reports."],
    docs=[],
    quiz=[q("What does a job architecture do?", ["Sets each person's salary", "Groups jobs by the kind and level of work", "Lists open requisitions"], 1, "It organizes jobs by the kind of work and the level of the work."),
          q("Where does a job's level show?", ["At the end of the job name", "Only in the position code", "On the requisition title"], 0, "The job name ends with its level within the growth stream, such as SS2."),
          q("Who matches a new role to a job?", ["The hiring manager", "Compensation, on the pre-search memo", "The recruiter"], 1, "Compensation matches duties to the job architecture.")])
NOTES["job-architecture"] = "From the SME review: split into two parts. Part 1 now defines job architecture and its key terms (job family and sub-family, growth stream, job level) and asks HCMs to review the positions in their area."

NEW["job-architecture-oracle"] = ("job-architecture", dict(
    slug="job-architecture-oracle", topic="recruiting", topic_label="Hiring",
    name="Job Architecture overview, Part 2: How our job architecture is set up in Oracle",
    title_pre="Job architecture,", title_em="part 2", system="Oracle HCM", time="4 min",
    sources=["Vanderbilt SME review, November 2026", "Job Architecture overview (HCM Academy, earlier edition)"],
    intro=["In Oracle, the job architecture lives on jobs, and jobs are attached to positions. Knowing which field is which keeps your positions and requisitions right.",
           "Read Part 1 first for the terms."],
    use_when="You are setting up or reading a position and need to know how the job, job code, and job name work in Oracle.",
    steps_title="How it shows up in Oracle",
    steps=[
        s("Job codes and position numbers are different.", "A job code ties a position to the university job architecture. A position number belongs to one seat (headcount) in a specific unit or division. The job code is assigned to the position; they are separate fields in Oracle."),
        s("Six-digit job codes are the job architecture.", "Staff and faculty jobs mapped to the job architecture have six-digit job codes. Not every worker type has been mapped yet: positions for students, postdocs, interns, affiliates, and contractors may still use other codes."),
        s("The job name carries its level.", "The job name ends with the job's level within its growth stream, such as Accountant Support SS2."),
        s("The job name becomes the business title.", "When someone is hired, their business title is the job name (for example, Program Manager 3), not the position name you chose. The requisition title is only the posting title, so you can make it clearer for candidates."),
        s("Skills come with the job.", "Core skills and skill levels are built into each job, so the requisition's Skills step pulls them in. You don't enter them."),
        s("Pay ranges are tied to the job.", "Each job will show its grade and pay range in Oracle. Some already do."),
    ],
    watch=["A requisition whose job code doesn't match the pre-search memo is sent back.",
           "Open item: confirm how positions for students, postdocs, interns, affiliates, and contractors are set up until they are mapped to the job architecture.",
           "Open item: confirm whether the University growth level is the same as the grade tied to compensation."],
    docs=[],
    quiz=[q("How do a job code and a position number differ?", ["They are the same field", "The job code ties to the job architecture; the position number is one seat in a unit", "The position number sets pay"], 1, "They are separate fields: the job code is assigned to the position."),
          q("A student position has no six-digit job code. What does that mean?", ["It must be deleted", "Not every worker type has been mapped to the job architecture yet", "It is a faculty position"], 1, "Six-digit codes are for staff and faculty jobs mapped so far."),
          q("What becomes the new hire's business title?", ["The position name", "The job name", "The requisition title"], 1, "The business title is the job name, such as Program Manager 3.")],
    pending=REVIEWED))
NOTES["job-architecture-oracle"] = "New course from the SME review: Part 2 of the job architecture overview, on how jobs, job codes, and position numbers are set up in Oracle."

REMOVED["new-vs-update-position"] = "create-position"
O["create-position"] = dict(
    intro=["Every hire starts with a position. The requisition is built from it, and the new hire's assignment inherits from it, so a mistake here follows the person all the way through.",
           "First decide whether you need a new position or an update to an existing one. Then have the position description and, for a staff position, the pre-search memo from Compensation."],
    use_when="You need a position to recruit and hire into, and you need to decide whether to create a new one or update one you have.",
    steps_insert={0: s("Decide: a new position or an update?", "Use the table below. A new role, or a seat in a different location or business unit, needs a new position. The same role changing, such as its name, job code, work unit, or location, is an update to the existing position (see Update a position).",
                       ["Positions can't move between business units.", "Fix the position before any requisition; the requisition copies it when submitted."])},
    steps_patch={7: s("Job: enter the job code from the pre-search memo.", "Search by code, not by name; the code returns the exact job (for example, Accountant Support SS2). The job name becomes the employee's business title and ties the position to Vanderbilt's job architecture, including pay ranges. Leave Manager blank: managers change, and the manager belongs on the assignment.",
                       ["Staff and faculty jobs mapped to the job architecture use six-digit codes.", "Not every worker type has been mapped yet; positions for students, postdocs, interns, affiliates, and contractors may use other codes."]),
                 9: s("Assignment category: the one on the memo.", "For staff positions, use the category on the pre-search memo. Most used: Professional exempt, Staff non-exempt, and VTS (Vanderbilt Temporary Services). Never Professional salaried non-exempt: it's built into Oracle but not used at Vanderbilt, and the position will be sent back."),
                 13: s("Attach the documents, add comments, and click Submit.", "For a staff position, central HR approves only with the pre-search memo attached (not needed for VTS). The position description helps your business unit approver. Attachments stay on the position, so you keep its history. Approval goes to your business unit approver (often the CFO), then to the central HR approval group.")},
    table=dict(title="New position or update?", head=["Situation", "Do this"], rows=[
        ["A new role in your business unit", "Create a new position"],
        ["More seats with the same job and location", "Use one pooled position (headcount more than 1)"],
        ["A seat in a different location", "Create a separate position"],
        ["The business unit changes", "Create a new position; positions can't move between business units"],
        ["A vacant position built for another worker type", "Create a new position; don't repurpose it"],
        ["An inactive position you want to use again", "Reactivate it only if it meets current guidelines; otherwise create a new one"],
        ["The same role's name, job code, category, work unit, or location changes", "Update the existing position"]]),
    watch_replace={0: "An inactive position that no longer meets current guidelines, such as one with an old job code, can block updates and approval. Bring it up to date or create a new one."},
    watch_add=["Fields that get positions sent back: Standard working hours (always 40), Job (the code from the memo), Assignment category (never Professional salaried non-exempt), Manager (leave blank), Attachments (the memo for a staff position).",
               "Open item: confirm the job code, assignment category, and pre-search memo rules for positions that are not staff positions (students, postdocs, interns, affiliates, contractors)."])
NOTES["create-position"] = "From the SME review: now includes when to create a new position or update one (the separate course is folded in), corrects job codes and the memo for positions that are not staff positions, and updates the video and job aid."

O["update-position"] = dict(
    intro=["Update a position when the role changes: its name, a reclassification with a new job code, its assignment category, its work unit (for example, when expenses are tracked differently), or its work location.",
           "Some changes reach the incumbent's assignment automatically once approved. Others don't, so plan a second transaction for those."],
    use_when="A position's name, job code, category, work unit, or work location changes, such as a reclassification.",
    steps_patch={2: s("Pick the action reason that matches the change.", "Updates have more reasons than new positions, for example a reclassification to a higher range, an assignment category change, or a work unit or location change. The reason drives reporting.")})
NOTES["update-position"] = "From the SME review: more reasons to update a position, such as a work unit change for expense tracking or a new work location. Video updated."

O["position-best-practices"] = dict(
    intro=["Most position approval errors come from using inaccurate or outdated positions and a few easy-to-miss fields. These habits keep positions active, clean, and correct, so Oracle shows what positions exist and their status."],
    steps_patch={
        0: s("Inactivate and reactivate on purpose.", "There are good reasons to inactivate a position you are not recruiting for, and to reactivate it when you need it again: it keeps vacant-position rosters accurate. Before you reuse a position, bring it up to current guidelines; an old position that no longer meets them causes send-backs.",
             ["Don't repurpose a vacant position built for another worker type. Create a new one."]),
        1: s("Use the job code from the memo.", "Staff and faculty jobs mapped to the job architecture use six-digit codes. Not every job has one yet, for example some student, postdoc, intern, affiliate, and contractor positions."),
        2: s("Request new positions through VU Compensation.", "Send the position description with the Vacant Reclassification/New Position Request Form or the Filled Reclassification Request Form to VU Compensation, not your engagement consultant. Requisitions need a memo from the last 12 months whose job code matches the position."),
        5: s("Set the real location.", "Use the position's primary office location, where most of the work takes place. It drives pay transparency, the pay range, and New York's background check process, and it informs decisions such as capacity, emergency management, and parking. One location per position.")},
    watch=["When in doubt about a code, category, or location, ask Compensation or your engagement consultant before you submit."],
    quiz=[q("You want to reuse an inactive position for a vacancy. What do you check first?", ["Nothing; reactivate it", "That it meets current guidelines and fits the worker type", "That it was inactive for under a year"], 1, "Reactivating is fine when the position meets current guidelines and the worker type fits."),
          q("Why leave Manager blank on the position?", ["Oracle requires it", "Managers change; the manager belongs on the assignment", "It speeds approval"], 1, "Keeping the manager on the assignment avoids stale history on the position."),
          q("Where do you request a new position?", ["Your engagement consultant", "VU Compensation, with the request form and position description", "Central recruiting"], 1, "New positions are requested through VU Compensation with the position description and the request form.")])
NOTES["position-best-practices"] = "From the SME review: when inactivating and reactivating positions is right, new positions requested through VU Compensation with the request forms, job codes for positions not yet mapped, and why location matters."

O["compensation-memo"] = dict(
    steps_patch={0: s("Write the position description.", "Use the standard Vanderbilt position description template."),
                 1: s("Request the review from VU Compensation.", "Send the position description with the Vacant Reclassification/New Position Request Form (a new or vacant position) or the Filled Reclassification Request Form (a filled position) to the Compensation team (vu.compensation@vanderbilt.edu). New positions are requested through VU Compensation, not your engagement consultant.")},
    watch_add=["Open item: confirm whether positions that are not staff positions (students, postdocs, interns, affiliates, contractors) need a pre-search memo."])
NOTES["compensation-memo"] = "From the SME review: new positions are requested through VU Compensation with the request forms and the position description, not through the engagement consultant. Video updated."

O["hire-staff"] = dict(
    steps_patch={1: s("Create the position (or update one that fits).", "Use the memo's job code, Standard working hours 40, the real location, and attach the memo. Don't repurpose a position built for another worker type, and reuse an inactive position only if it meets current guidelines. See: Create a position.")},
    keep_pending=True)
NOTES["hire-staff"] = "Matched to the SME review of Position best practices: reuse an inactive position only if it meets current guidelines. Video updated."

O["convert-pending-worker"] = dict(
    steps_patch={5: s("Biographical info: confirm date of birth and citizenship.", "Date of birth comes from the background check. US citizen or permanent resident looks complete until you click the pencil: always click it and pick Yes or No. PEBC records the answer on the application.")},
    watch_add=["The citizenship field doesn't look like it needs data. Click the pencil every time."])
NOTES["convert-pending-worker"] = "From the SME review: the citizenship field must be opened with the pencil, or it's easy to miss."


# ───────────── 02 Payroll & Timecards ─────────────
CAL = ("Vanderbilt: Pay Calendar (People Experience)", "https://hr.vanderbilt.edu/compensation/payroll-calendar/")

O["hcm-role-in-payroll"] = dict(
    steps_patch={
        1: s("Exempt (monthly) staff: hands off, with two exceptions.", "Monthly salaried pay runs from the salary on the record. You only act when something extra is being paid or something has gone wrong.", ["Add a compensation payment when needed, such as a lump sum.", "Work an issue with payroll when one comes up."]),
        2: s("Weekly and biweekly employees: check time cards every week.", "Hourly pay depends on submitted, approved time cards. A missing time card means a missing or short paycheck, so this is the one recurring payroll task that is yours.",
             ["Confirm every time card is submitted.", "Follow up with line managers on missing or late time cards.", "Payroll usually notifies the line manager when a time card isn't approved.", "Escalate errors you can't resolve to payroll."]),
        3: s("Errors: you fix them, and work with payroll when you need more information.", "Correct the record yourself unless you need information only payroll has, such as an overpayment amount. When a correction needs an off-cycle payment, you submit the off-cycle request, and payroll approves or denies it.")},
    watch=["HCMs can't run or rerun payroll. That is payroll's job.",
           "Open item: Payroll is still documenting which payroll elements you should confirm on the record at hire.",
           "Open item: confirm whether line managers or HCMs keep up with late and missing time cards, since payroll usually notifies the line manager."],
    docs=[],
    quiz=[q("Who runs the payroll cycle?", ["The HCM", "Payroll", "The employee's manager"], 1, "Payroll runs payroll. HCMs make sure records and time cards are right so it can run."),
          q("For exempt (monthly) staff, when does the HCM step in?", ["Every pay period, to approve hours", "Only to add a compensation payment or fix an issue", "Never"], 1, "Exempt pay is hands off unless you are adding a payment, such as a lump sum, or working an issue."),
          q("A correction needs an off-cycle payment. Who does what?", ["You submit the off-cycle request; payroll approves or denies it", "Payroll finds and fixes it on its own", "The employee requests it"], 0, "You fix the record and submit the request. Payroll decides.")])
NOTES["hcm-role-in-payroll"] = "From the SME review: exempt guidance is for staff, follow up with line managers, HCMs fix errors and submit off-cycle requests that payroll approves or denies, and an unhelpful link removed."

O["weekly-time-card-check"] = dict(
    intro=["If you support weekly or biweekly employees, run this check every week so no one is paid late or wrong.",
           "In UKG, the employee submits the time card, the line manager approves it, and payroll signs it off before payroll runs. Sign-off is payroll's last step: after it, an approval can't be removed unless payroll removes the sign-off first. Your check makes sure nothing is stuck before sign-off."],
    steps_patch={
        0: s("Open UKG from Oracle.", "Sign in to Oracle Cloud with your VUnetID. On the Home page, on the Me tab, under Apps, select UKG (Kronos) Timesheets. UKG opens on its Home page. If you don't see employees you support, your access isn't set up yet: contact payroll.", ["Don't see UKG on the Me tab? Select + under Apps; it may be one of the apps not shown."]),
        5: s("Missing or late time card: contact the line manager.", "Email or call the line manager with the employee's name, the pay period, and what's missing (for example, \"no punches Tuesday\"). Ask them to correct and approve it before the deadline on the payroll calendar. Time cards are due at noon on the Monday after the pay period ends; holiday weeks move it.")},
    watch_add=["Open item: add the UKG report that lists time cards not yet submitted, and how to schedule it."],
    docs=[])
NOTES["weekly-time-card-check"] = "From the SME review: who submits, approves, and signs off, what sign-off means, a tip for finding UKG on the Me tab, line manager wording, and a link meant for managers removed."

# the four UKG courses become one
for _x in ("review-approve-time-cards", "enter-pto", "ukg-for-managers", "ukg-for-employees"):
    REMOVED[_x] = "ukg-time-cards"
NEW["ukg-time-cards"] = ("weekly-time-card-check", dict(
    slug="ukg-time-cards", topic="payroll", topic_label="Payroll & Timecards",
    name="UKG time cards and time off (non-exempt)", title_pre="UKG time cards and", title_em="time off",
    system="UKG (Kronos)", time="10 min",
    sources=["Vanderbilt SME review, November 2026", "Review and approve time cards, Enter PTO, and the UKG manager and employee courses (HCM Academy, earlier edition)"],
    intro=["Non-exempt (weekly and biweekly) pay depends on UKG time cards. The employee submits, the line manager approves, and payroll signs off before payroll runs.",
           "Your part as the HCM is to check, follow up, and step in when an employee can't enter their own time. Approving is the line manager's job."],
    use_when="You are checking non-exempt time for a pay period, entering hours or PTO for an employee who can't, or helping a manager or employee in UKG.",
    steps=[
        s("Open UKG from Oracle.", "On the Oracle Home page, on the Me tab, under Apps, select UKG (Kronos) Timesheets. If you don't see employees you support, your access isn't set up yet: contact payroll.", ["Don't see UKG? Select + under Apps; it may be one of the apps not shown."]),
        s("Know the approval chain.", "The employee submits their time card, the line manager approves it, and payroll signs it off. After sign-off, an approval can't be removed unless payroll removes the sign-off first.", ["Employee submits", "Line manager approves", "Payroll signs off"]),
        s("Open the time cards for your employees.", "On the UKG Home page, scroll to Links and select By Pay Period. It opens on the most recently completed pay period, one row per employee. Use the arrow next to Pay Period to move to the current one.",
          ["Filter: type your business unit under Business Unit (or your work unit under Work Unit), then select Refresh.", "Tip: filter by Approval State to find time cards that should be submitted and aren't."]),
        s("Check each employee's status, hours, and exceptions.", "The Approval State column shows Open, Submitted, or Approved (PayPrep Ready). Exceptions such as a missing punch show in color. Ask the line manager to resolve exceptions before they approve."),
        s("Submit for an employee who couldn't.", "Check the box next to the employee and choose Submit. Then the line manager approves it, not you. Reject sends a time card back so it can be corrected."),
        s("Enter hours or PTO for an employee.", "Open the time card and add a new row on the day (the + icon); a pay code can't go on a row that already has punches. In the Time Off column, select Browse and pick the pay code, such as PTO-Vacation or PTO-Sick. Enter the hours: non-exempt PTO goes in 4-hour increments.",
          ["Then select Save at the top right. In an open period, Save only; don't Submit."]),
        s("Confirm the entry saved.", "Close the time card and open it again. The row should show the pay code and hours. If it's missing, the save didn't go through: enter it again."),
        s("Time off requests: check what's pending.", "Employees request time off in UKG. The line manager approves or refuses each request in Control Center, under employee requests. Only approved time off appears on the time card, so look for requests still pending."),
        s("Use schedules where they exist.", "A schedule shows when the employee was expected to work, so you can compare it with the punches. Not everyone has a schedule in UKG."),
        s("Follow up until every time card is approved.", "Check every week for weekly employees and every pay period for biweekly employees, until every time card shows Approved. Time cards are due at noon on the Monday after the pay period ends; holiday weeks move it."),
        s("Help employees with their own time cards.", "Undergraduates and non-exempt staff can enter time and request time off on the UKG website or the mobile app, and so can approvers. Employees save during the period and submit when it is complete."),
    ],
    table=dict(title="Approval State column", head=["State", "What it means for you"], rows=[
        ["Open", "Not submitted yet; follow up with the employee and line manager"],
        ["Submitted", "The employee is done; the line manager still needs to approve"],
        ["Approved (PayPrep Ready)", "Ready for payroll; no action needed"]]),
    watch=["Empty time cards early in an open period are normal.",
           "In an open period, Save. Don't Submit. Submitting means you must edit, update, and resubmit later.",
           "One person does not both submit and approve the same time card. If you submit for an employee, the line manager approves it.",
           "Exempt employees' time off is managed in Oracle, not UKG.",
           "Open item: Payroll to confirm the rule that the person who submits a time card does not approve it, and who approves when the manager is out.",
           "Open item: confirm the label for turning down a time off request (Refuse or Reject).",
           "Open item: document how a manager approves every line an employee submitted (select all, approve, then submit or approve again).",
           "Open item: add how to add a schedule in UKG, and how to save a view that lists your student workers first."],
    docs=[("UKG: Request Time Off from My Calendar (employees)", "https://communityfiles.ukg.com/support/kol/onlinehelp-workforcedimensions/en-us/Content/Employee/TimeOffRequest.htm"),
          ("UKG: Respond to time-off requests in Control Center (managers)", "https://communityfiles.ukg.com/support/KOL/OnlineHelp-WorkforceDimensions/en-us/Content/ControlCenter/ApproveATimeoffRequest.htm")],
    quiz=[q("What is the approval chain for a UKG time card?", ["Employee approves, manager approves, payroll signs off", "Employee submits, line manager approves, payroll signs off", "HCM approves, payroll signs off"], 1, "The employee submits, the line manager approves, and payroll signs off."),
          q("You entered PTO in an open period. What do you click?", ["Submit", "Save", "Approve"], 1, "Save only. Submitting in an open period means editing and resubmitting later."),
          q("You submitted a time card for an employee who couldn't. Who approves it?", ["You", "The line manager", "No one; payroll signs off next"], 1, "The person who submits a time card does not approve it."),
          q("Which pay codes can you pick for PTO?", ["PTO-Vacation or PTO-Sick", "Only PTO-Vacation", "Any pay code"], 0, "Pick the PTO type the employee asked for, such as PTO-Vacation or PTO-Sick.")],
    pending=REVIEWED))
NOTES["ukg-time-cards"] = "New course from the SME review: Review and approve time cards, Enter PTO, and the UKG courses for managers and employees are now one course, with the approval chain corrected (the employee submits), PTO-Sick, the mobile app, and broken links removed."

O["off-cycle-payment"] = dict(
    intro=["When a transaction fails to pay through no fault of the employee, such as an Oracle glitch or a missed handoff, an off-cycle payment gets the employee paid before the next regular payroll.",
           "Payroll pays these with Oracle's QuickPay process. Your part is the transaction and the request. This is the only way exempt staff get paid outside the monthly payroll."],
    use_when="A transaction failed to pay and it was not the employee's fault.",
    steps_patch={
        0: s("Submit, or resubmit, the Oracle transaction, and wait for full approval.", "Payroll can only pay what is on the record. Find the transaction that failed and submit it again, or fix and resubmit it. You can't request an off-cycle payment until the transaction is fully approved.",
             ["Check its status: select the bell, then See more. On the notifications page, the Created by me tab shows what you submitted. Open it; the bottom of the window shows where it is in approval."]),
        1: s("Open the off-cycle paycheck request form.", "The form is at forms.vanderbilt.edu (see the link under Official documentation). Bookmark it. It is how payroll knows a person needs a QuickPay run."),
        4: s("Submit the form.", "You receive an email copy of the request. Keep it so you can follow up."),
        5: s("Let payroll review it.", "Payroll reviews the request and approves it, or tells you by email when it will be paid. Contact payroll only if you haven't heard back in a while or the deadline is close.",
             ["Close to the payroll deadline, you can email payroll and ask them to put the payment on their watch list."]),
        6: s("Confirm the payment.", "Payroll pays it in the next off-cycle run, to direct deposit. Tell the employee when to expect it, then check their payslip to confirm the payment came through.")},
    watch_add=["Open item: list when to use each reason on the form."],
    docs=[("Vanderbilt: Off-cycle paycheck request form", "https://forms.vanderbilt.edu/view.php?id=829931"), CAL])
NOTES["off-cycle-payment"] = "From the SME review: not the employee's fault (rather than also the HCM's), the transaction must be fully approved first, the form link, the email copy, the watch list, and checking the payslip."

O["change-salary"] = dict(
    topic="positions", topic_label="Assignment Changes",
    steps_patch={
        0: s("Open Change Salary for the employee.", "On the Home page, go to Our Workforce, then Quick Actions (Show More if you don't see it), and choose Change Salary. Type the employee's name or person number and press Enter, then choose the effective date so you see the right assignments. If the person has more than one assignment, check the job title and work unit so you pick the right one.",
             ["Quick Actions > Change Salary > select the employee, or", "Search the employee's name > Change Salary."]),
        7: s("Add comments and attachments, then click Submit.", "Write a short explanation of why the change is happening, as if the approver has no backstory, so they don't have to come back with questions. Then attach the documents and select Submit. Track it from the notifications bell.")},
    table_add_row=["Annual increase", "Only in the annual increase process, not for off-cycle changes."],
    watch_add=["Open item: explain when to use the supporting documents section and when to use attachments."],
    docs=[])
NOTES["change-salary"] = "From the SME review: moved to Assignment Changes; press Enter and set the effective date when you search, explain the change for the approver, and unhelpful links removed."

O["net-one-time-stipend"] = dict(
    steps_patch={
        0: s("Open Individual Compensation for the employee.", "On the Home page, go to Our Workforce and search the employee's name. Enter the effective date before you search further, find the correct assignment, select the three dots, then Individual Compensation. It lists any payments already awarded.",
             ["Or: Quick Actions > Individual Compensation > select the employee."]),
        7: s("Click Continue, add comments and documentation, then Submit.", "Always attach documentation and say what the payment is for. Then select Submit and track approval from the notifications bell.")},
    watch_add=["Open item: how you know when to ask payroll about Process separately.",
               "Open item: confirm with payroll that two payments for the same month can't be on the same assignment."],
    docs=[])
NOTES["net-one-time-stipend"] = "From the SME review: the effective date and assignment in the first step, documentation always attached, and unhelpful links removed."

O["sign-on-bonus"] = dict(
    steps_patch={
        0: s("Open Individual Compensation for the employee.", "Search the employee's name from Our Workforce, enter the effective date, and pick their assignment, then choose Individual Compensation. The payment needs an open assignment; if there isn't one, an assignment must be created first. Bonuses go here, not Change Salary, because they are not part of base pay."),
        3: s("Start and end dates: the target payroll month.", "Enter the first day of the month you're paying in as the start date (for example, Nov 1). A one-time payment also needs an end date: select the option to show the end date field, then enter it. The bonus pays in the payroll covering these dates, if it is entered before the cutoff."),
        6: s("Click Continue, add comments and attachments, then Submit.", "Attach the offer or bonus letter; documentation is required. File the signed letter as a Compensation Letters document record. Track approval from the notifications bell.")},
    watch_add=["Open item: add the award compensation guide to this course.", "Open item: confirm whether this course covers bonuses for students as well as staff."],
    docs=[])
NOTES["sign-on-bonus"] = "From the SME review: the effective date and an open assignment, start and end dates, documentation required, and open items on the award compensation guide and students."

O["comp-impacts-payroll"] = dict(
    steps_insert={6: s("Check costing with every pay change.", "Costing decides where the pay is charged. Review it whenever pay changes (see Costing Management).")},
    watch_add=["Close to the payroll deadline, you can email payroll and ask them to put a payment on their watch list."],
    docs=[CAL])
NOTES["comp-impacts-payroll"] = "From the SME review: a link to the payroll calendar, the payroll watch list, costing, and links replaced."


# ───────────── 05 Costing Management ─────────────
GLOSSARY = dict(title="Costing terms", head=["Term", "What it means"], rows=[
    ["FUM", "Financial Unit Manager: your finance contact for costing"],
    ["COA string", "Chart of Accounts string: entity, net asset class, financial unit, program, activity, and function"],
    ["POET string", "Project, Organization, Expenditure Type, and Task: the string for grants and other projects"],
    ["Element", "One type of pay within an assignment, such as a lump sum"],
    ["Suspense", "Where a charge goes when its costing string is wrong or has a blank segment"],
    ["RCT", "Retro cost transfer: moves dollars already charged after payroll has run"]])

O["costing-fundamentals"] = dict(
    intro=["Payroll costing decides which costing string (COA or POET) pays for a person's compensation, and for which periods. It matters for all sponsored research, including grants and contracts, and for faculty funds, gifts, endowments, capital projects, and cores, many of which use task numbers.",
           "An assignment with no costing is not an error: the work unit default applies. A mistyped costing string with a blank segment is different: it doesn't default, it goes to suspense."],
    steps_patch={
        0: s("Know the three levels Vanderbilt uses.", "Vanderbilt's guide calls this the labor cost inheritance pyramid. Oracle uses the most specific costing it finds: element, then assignment, then the work unit default.",
             ["Element (a type of pay within the assignment, such as a lump sum): if costed, that pay is charged to the element's costing string. This is how you charge a lump sum to a different department.",
              "Assignment (the person's job): if costed, all pay on the job follows it, except elements costed on their own.",
              "Work unit default: with no specific costing, pay goes to the work unit's entity and financial unit, general unrestricted funds (05), the natural account for that type of pay, and program and activity 000."]),
        3: s("Select the person, then select an element or assignment on the left.", "You only see costing after you select an element or an assignment on the left, in Costing for a Person Overview. A green check next to one means it has costing for the date you searched. The right side, Cost Accounts, shows the costing lines."),
        5: s("Ask your FUM whether your area uses program and activity codes.", "Some schools use program and activity codes to separate costs within a COA. If yours does, people need costing entered with the right codes; otherwise they default to program and activity 000."),
        6: s("Ask your FUM or grants manager whether effort must be costed to a POET string.", "This step must be right. You may not know how each person spends their time, so work with your FUM or grants manager to decide when costing is needed and how much effort goes to each costing line. Then get the COA or POET string and enter it (see Enter costing for a person).")},
    table=GLOSSARY,
    watch=["Costing affects budgets, and some costing changes can't be corrected. Validate with your FUM.",
           "Costing touches payroll and financial reporting. Wrong costing charges the wrong budget.",
           "Open item: explain how a department sets default costing at the work unit or business unit level.",
           "Open item: confirm whether default costing shows on the costing reports or appears blank. Some schools cost everyone.",
           "Open item: replace the program code example with one most areas recognize, and link the costing by person information."],
    quiz=[q("An assignment has no costing. What happens?", ["Payroll fails", "Salary charges to the work unit's default costing", "The employee isn't paid"], 1, "Blank costing on an assignment means the work unit default applies."),
          q("A costing string is mistyped and one segment is blank. What happens?", ["It defaults to the work unit", "The charge goes to suspense", "Oracle fixes it"], 1, "A wrong or incomplete string doesn't default. It goes to suspense."),
          q("Who helps you decide whether effort must be costed to a POET string?", ["The recruiter", "Your FUM or grants manager", "The employee"], 1, "Work with your FUM or grants manager; they know the funding.")])
NOTES["costing-fundamentals"] = "From the SME review: costing terms (FUM, COA, POET, suspense, RCT), every kind of funding that needs costing, a mistyped string goes to suspense, program and activity codes, and working with the FUM or grants manager on effort."

O["costing-impacts"] = dict(
    intro=["Costing tells Oracle which costing strings pay for a person's salary. Each payroll run turns pay into costing results that move to the General Ledger, so wrong costing means wrong department, grant, and project financials.",
           "Fixing costing after payroll runs takes a retro cost transfer, so getting it right up front saves everyone time."],
    steps_patch={
        0: s("Costing is set in Costing for Persons.", "Costing for Persons holds the costing for a person. Review and update it when someone is hired or transfers, when funding changes (including new projects), when effort allocation or task numbers change, or when costing was wrong."),
        3: s("Costing must be right before payroll runs.", "This covers everything costed to a POET string, not only grants. The costing has to be right before payroll starts the run that moves the dollars to the ledger. Costing lines must total 100%; Oracle won't let you leave the costing screen with less."),
        4: s("Costing follows a person who transfers business units (BUs).", "The old costing follows the employee to the new business unit. The HCM in the new business unit updates the costing so pay is charged correctly from the transfer date, and HCMs in both areas confirm it was updated."),
        5: s("After payroll runs, a retro cost transfer (RCT) is needed.", "If costing has to change for pay already processed, start a retro cost transfer. RCTs must meet certain criteria, and they need two things: the costing updated in Oracle, and the RCT form that moves the actual dollars.")},
    watch=["After a business unit transfer, costing does not reset on its own. Review it every time.",
           "Blank costing on an assignment is not wrong by itself; the work unit default applies. Confirm the default is where the pay should go.",
           "Open item: confirm the criteria for retro cost transfers and the deadline to fix costing before a payroll run. This covers more than grant labor."],
    quiz=[q("An employee transferred from another BU. Who updates their costing?", ["Nobody; it resets automatically", "The HCM in the new business unit, and both HCMs confirm it", "Payroll"], 1, "Costing follows the person; the HCM in the new area updates it."),
          q("Costing needs to change for a pay period already paid. What is needed?", ["Nothing; Oracle recalculates", "A retro cost transfer: the Oracle costing update and the RCT form", "An off-cycle payment"], 1, "An RCT needs both the costing update and the form that moves the dollars."),
          q("Element costing and assignment costing disagree. Which wins?", ["Element", "Assignment", "Work unit default"], 0, "The order is element, then assignment, then work unit default.")])
NOTES["costing-impacts"] = "From the SME review: costing strings rather than accounts, every POET-funded item, 100% before payroll, who updates costing after a transfer, and retro cost transfers."

O["when-to-update-costing"] = dict(
    intro=["Changes to an employee's job or funding may require an update to their payroll costing in Oracle. Learn the events that should send you to check costing."],
    steps_patch={
        1: s("New hire: is the costing right for every funding source?", "Check on day one so the first paycheck charges the right place. Question every type of funding, not only the program code. Search on the hire date; a new hire won't appear if you search on an earlier date."),
        2: s("A change within the work unit: is the funding still correct?", "The work unit default doesn't change, but the funding may. Check every type of funding, not only the program code. If it changed, use Edit > Update from the first day of the pay period the change takes effect."),
        3: s("Transfer to another work unit or business unit: the new area updates costing.", "Existing costing follows the employee; it doesn't reset. The HCM in the new area is responsible for updating the costing string (see Enter costing for a person for Update and End Date). Search on the first day of the pay period the transfer takes effect."),
        4: s("Bonus, lump sum, or interim pay: should it charge a different funding source than salary?", "If yes, cost the element so only that payment goes to the other funding source. The salary stays where it is."),
        5: s("Another business unit funds an award for your employee.", "The HCM who owns the employee enters the award compensation and its costing, based on an email request from the funding business unit. Get the request in writing."),
        6: s("Salary distributed across multiple funding sources.", "Enter two or more costing lines that total 100%. Oracle won't let you leave the costing screen until they do."),
        7: s("Before every HCM Transaction Cutoff: check costing for your unit.", "Run the Cost Allocation Verification Report; it flags mismatched data, so run it before the payroll cutoff. The HCM Assignment Cost Allocation Plan report shows the costing that will apply.")},
    watch=["Costing follows an employee who changes business units. The HCM receiving the transfer reviews the COA and POET costing so payroll is charged to the new funding source.",
           "Most of these scenarios don't have walkthroughs recorded yet. Ask your FUM when unsure.",
           "Salary distributed across multiple funding sources and cross-unit award compensation may become reference resources rather than core training. To be decided by the HCM group."],
    quiz=[q("An employee moves to a different team in the same work unit. What do you check?", ["Nothing", "That every funding source in their costing is still correct", "Their salary"], 1, "Funding can change even when the work unit doesn't."),
          q("A bonus should charge a different funding source than salary. What do you cost?", ["The element (the bonus)", "The whole assignment", "Nothing"], 0, "Cost the bonus element so only that payment goes to the other funding source."),
          q("Another business unit funds an award for your employee. Who enters it?", ["The funding business unit", "You, the HCM who owns the employee, with their request in writing", "Payroll"], 1, "The owning HCM enters the award and its costing, based on the written request.")])
NOTES["when-to-update-costing"] = "From the SME review: every type of funding (not only program codes), who updates costing after a transfer, who enters cross-unit awards, salary across multiple funding sources, and the Cost Allocation Verification Report."

REMOVED["change-existing-costing"] = "enter-edit-costing"
O["enter-edit-costing"] = dict(
    intro=["Use Costing for Persons to enter or change where an assignment, or a single pay element, is charged. You need the HCM role in Oracle to enter costing; a FUM can't unless they have that role too.",
           "Get the COA or POET string from your FUM before you start. Costing for an assignment and costing for an element are different tasks."],
    use_when="The default won't work and a person or a payment needs specific costing, or existing costing needs to start differently, be fixed, stop, or be removed.",
    time="12 min",
    steps=[
        s("Open Costing for Persons.", "On the Home page, go to Our Workforce, then Costing for Persons (a quick action). A person search page opens."),
        s("Search the person with Advanced Search and the right Effective As-of Date.", "Costing is date-effective, so the date you search on is the date your entry applies to. Type the person's name, select Advanced Search, open Effective As-of Date, enter the date, select OK, then search.",
          ["Use the Pay Period Begin Date (from the payroll calendar) of the period the costing should start.", "A future-dated change: enter that future date.", "End Date: search on the last day of the last pay period the costing should apply.", "Prior pay periods also need the retro form; see the watch-outs."]),
        s("Select the person, then review the costing History.", "Select the assignment or element on the left to see its costing. Select History (top right) to see every past, current, and future costing period before you change anything."),
        s("Cost the assignment.", "Select the assignment, then Actions above the tree, then Create, then Create Costing. Check the Effective Start Date above the costing lines."),
        s("Cost an element.", "Select the assignment, then Actions above the tree, then Create, and add the element (Create Costing of Element). Pick the Element Name ending in Earnings Results (for example, BON Earnings Results). Codes are in the HCM Award Compensation Resource Guide on the HCM Specialist resource page."),
        s("Change existing costing with Edit.", "Select Edit, then the action (see the table): Update for a current or future change, Correct to fix a previous costing for its whole period, End Date to stop it, or Delete Record to remove it. Check the Effective Start Date above the costing before you save."),
        s("Enter each costing line. Percentages must total 100%.", "Each line is one costing string and a percentage. Oracle does not validate COA or POET strings, so check every value against what your FUM gave you.",
          ["Whole percentages are recommended; decimals are allowed, for example for grant cost share.",
           "COA string: Entity, Net Asset Class (for example, 05), Financial Unit, Program and Activity (000 if unused), VU_Function. Use default zeros for InterEntity (000), Future 2 (0), and the POET fields (0000). Leave Allocation Type blank.",
           "Account: for an element, enter it: 5110 faculty, 5120 staff, 5130 student.",
           "POET string (grants and projects): in the COA fields, enter the payroll clearing string 380.05.38600.5140.000.000.000.VUI.0, then Project Number, Organization, Expenditure Type (SalFac, SalStaff, or SalStud), and Task. Leave Allocation Type blank."]),
        s("Select Submit.", "If you see a warning that percentages are under 100%, select Cancel and fix them. There's no approval workflow, so you won't get a notification. After you submit, Oracle returns you to the Home page."),
        s("Run the Cost Allocation Verification report.", "The report (in the Departmental Playbook) lists entries with common COA or POET errors. If one of yours appears, correct it before the payroll deadline. Left uncorrected, it could affect the employee's paycheck or send the charge to a suspense account."),
    ],
    table=dict(title="Change existing costing: which action, which search date", head=["Action", "Use it to", "Search on"], rows=[
        ["Update", "Start a different costing as of a date. History is kept and a new record is added.", "First day of the pay period the new costing starts"],
        ["Correct", "Revise an existing costing for its entire date range.", "First day of the pay period it should have started"],
        ["End Date", "Stop costing as of a pay period end date.", "Last day of the last pay period it should apply"],
        ["Delete Record", "Remove a costing record completely.", "First day of the pay period of the record to remove"]]),
    watch=["Costing applies to a full pay period. Oracle uses the costing in effect on the Pay Period End Date and does not prorate.",
           "Current and future changes: enter by the HCM Transaction Cutoff.",
           "Prior periods: also submit the Retro Costing Request Form (Salary) to the Research Finance Team by the Retro Change Cutoff, usually two business days before the HCM Transaction Cutoff. Include a cost transfer memo if an externally funded grant is affected.",
           "Don't End Date a prior period if you want to keep costing records that come after that date. End Date ends everything from that date forward. After End Date, use Create, not Update, to add costing again.",
           "Open item: confirm whether Oracle fills in the account for a COA string on an assignment.",
           "Open item: confirm whether the Retro Costing Request Form is the retro cost transfer (RCT) form, and its criteria.",
           "Open item: bring back the costing visual from the Oracle implementation, updated."],
    quiz=[q("You need to cost a change that starts next pay period. What date do you search on?", ["Today", "The Pay Period Begin Date of the period it starts", "The last day of this month"], 1, "Costing is date-effective; search on the date it should start."),
          q("Costing was entered wrong for the whole Nov 1 forward period. Which action?", ["Update", "Correct", "Delete Record"], 1, "Correct revises the existing costing for its entire date range."),
          q("You're costing a bonus element for a staff member. What goes in Account?", ["Leave it blank", "5120", "5140"], 1, "Element costing needs the Account: 5110 faculty, 5120 staff, 5130 student."),
          q("The verification report lists one of your entries. What do you do?", ["Wait for payroll to fix it", "Correct it before the payroll deadline", "Delete the person's costing"], 1, "Uncorrected errors can affect pay or send the charge to suspense.")])
NOTES["enter-edit-costing"] = "From the SME review: Change existing costing is folded in; costing an assignment and costing an element are separate steps; the HCM role is needed; Pay Period Begin Date for searches; FUM; and the verification report's consequences."


# ───────────── 07 Document Records & Reporting ─────────────
LEAVE_ELSEWHERE = "Leave and accommodation records, including New York Unpaid Sick Leave, Prenatal Leave, and Paid Family Leave documentation, are stored outside Oracle Document Records. Never upload medical or protected health information to Oracle."
O["add-document-record"] = dict(
    intro=["Signed documents belong in the employee's personnel file in Oracle, as document records. A document record is the file plus details about it: its type, name, and the dates it covers.",
           "HCMs upload employment agreements, written and final discipline letters, PIP documents, reclassification and compensation letters, and resignation letters or emails. Leave and accommodation records are stored elsewhere."],
    use_when="You have a final, signed document to file: an employment agreement, a written or final discipline letter, a PIP document, a reclassification or compensation letter, a resignation letter or email, or a New York wage notice.",
    table_replace_row=(3, ["Not in Oracle Document Records", LEAVE_ELSEWHERE]),
    table_add_row=["New York wage notices", "New hire and wage change notices. HCMs upload them while automation is in development."],
    watch=["Attach only the final signed copy.",
           "Do not upload medical or protected health information to Oracle Document Records.",
           "Questions about which type to use go to your HR Consultant.",
           "Open item: confirm the document types for employment agreements, resignation letters, and New York wage notices.",
           "Confirm the exact Document Records menu path in Vanderbilt's Oracle during a recorded demo."],
    quiz_patch={2: q("An employee's leave approval letter arrives. Does it go in Oracle Document Records?", ["Yes, as a Compensation Letter", "No, leave and accommodation records are stored elsewhere", "Yes, as a Performance Review"], 1, "Leave and accommodation records are stored outside Oracle Document Records, and medical information never goes there.")})
NOTES["add-document-record"] = "From the SME review: what HCMs upload (including New York wage notices), leave and accommodation records stored outside Oracle, and no medical or protected health information in Oracle."

O["fmla-tmla-transactions"] = dict(
    steps_patch={6: s("Store the approval letter where Vanderbilt keeps leave records.", LEAVE_ELSEWHERE)},
    watch_add=["Open item: confirm where leave and accommodation records are stored, and who stores them."],
    quiz_patch={1: q("An approved FMLA letter arrives. Where does it go?", ["Oracle Document Records", "Where Vanderbilt stores leave records, outside Oracle Document Records", "A comment on the payroll calendar"], 1, "Leave records are stored outside Oracle Document Records.")},
    keep_pending=True)
NOTES["fmla-tmla-transactions"] = "From the Records SME review: leave approval letters are stored outside Oracle Document Records, and medical information never goes in Oracle."

# ───────────── 03 Assignments and 06 Students & Faculty ─────────────
O["add-assignment"] = dict(topic="students", topic_label="Students & Faculty", keep_pending=True)
NOTES["add-assignment"] = "From the SME review: moved to Student and Faculty Hiring and Assignments."

# screen checks for the courses the review created or reshaped
VERIFY["ukg-time-cards"] = ["the pay code names in the Time Off list (PTO-Vacation, PTO-Sick)", "who to contact when UKG access is missing",
    "the label for turning down a time off request (Refuse or Reject)", "the Control Center and schedule screens managers use"]
VERIFY["job-architecture-oracle"] = ["where job code and position number show on the position", "how positions not yet mapped to the job architecture are coded"]
VERIFY["enter-edit-costing"] = ["where Costing for Persons sits in Redwood", "the Advanced Search and Effective As-of Date labels", "the Actions, Create, and Edit menu labels",
    "whether Oracle fills in the account for a COA string", "that a regular HCM (not a super-user) sees Our Workforce and this quick action"]

# ───────────── apply ─────────────
def apply(courses):
    for slug, (after, c) in NEW.items():
        i = next(k for k, x in enumerate(courses) if x["slug"] == after)
        courses.insert(i + 1, c)
    courses[:] = [c for c in courses if c["slug"] not in REMOVED]
    by = {c["slug"]: c for c in courses}
    for slug, o in O.items():
        if slug not in by: continue
        c = by[slug]; o = dict(o)
        for i, st in sorted(o.pop("steps_insert", {}).items()): c["steps"] = c["steps"][:i] + [st] + c["steps"][i:]
        for i, st in o.pop("steps_patch", {}).items(): c["steps"][i] = st
        for i, w in o.pop("watch_replace", {}).items(): c["watch"][i] = w
        c["watch"] = c["watch"] + o.pop("watch_add", [])
        if "table_replace_row" in o:
            i, row = o.pop("table_replace_row"); rows = list(c["table"]["rows"]); rows[i] = row; c["table"] = dict(c["table"], rows=rows)
        for i, qq in o.pop("quiz_patch", {}).items(): c["quiz"] = c["quiz"][:i] + [qq] + c["quiz"][i + 1:]
        if "table_add_row" in o: c["table"] = dict(c["table"], rows=c["table"]["rows"] + [o.pop("table_add_row")])
        keep = o.pop("keep_pending", False)
        c.update(o)
        if not keep: c["pending"] = REVIEWED
    return courses
