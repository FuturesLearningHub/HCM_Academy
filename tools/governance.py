# Course governance for HCM Academy: who owns each course, what changed and when, and the
# "Before you submit" block (what to attach, what to check, which cutoff applies, who does what).
# One source for tools/build_courses.py, tools/build_playbook.py, tools/build_section_audit.py and
# the two table courses in tools/courses_v02.py (What to attach, Who owns what).
#
# Why this exists: wrong or incomplete data in a hire or a pay change reaches payroll. Getting it right
# takes standard documents and checks for each transaction, guidance that says when it last changed,
# a clear owner, and a watch on the errors that keep coming back. Everything here is a DRAFT for the
# owners to confirm.
#
# Rules: no em or en dashes. Every item is taken from a course in tools/course_content.py or
# tools/courses_researched.py. Where the courses do not say, the entry says so ("to confirm") instead
# of guessing. No individual names: owners are teams. The contact for each team is in the owner
# register, which is kept outside this repository.

EDITION = "V.02 draft"
EDITION_MONTH = "November 2026"
UPDATED = "Nov 12, 2026"        # when the V.02 draft was first published
OWNERS_SET = "Nov 13, 2026"     # when owners were set to the teams: Payroll and HRIS
SCREENS = "Nov 17, 2026"       # videos added; corrections from Vanderbilt's Our Workforce screens
REVIEWED_ON = "Nov 18, 2026"   # Vanderbilt SME review applied (tools/reviews.py)
LATEST = REVIEWED_ON            # the newest change across all courses
FIRST = "October 2026"          # when the V.01 courses were first drafted

# ───────────── Owners ─────────────
# Payroll owns all payroll and financial topics. HRIS owns everything else: recruiting and hiring,
# assignment changes, offboarding, leave, records and reporting, and the foundations.
PAY, HIRE, TBD = "Payroll", "HRIS", "To be named"   # TBD is for a future course that has no owner yet
OWNER_SCOPE = {
    PAY: "All payroll and financial topics: payroll, time cards, pay changes, the payroll calendar, and costing.",
    HIRE: "Recruiting and hiring, assignment changes, offboarding, leave, records and reporting, and the HCM foundations.",
    TBD: "No owner yet.",
}
_BY_TOPIC = {"payroll": PAY, "costing": PAY}
_BY_SLUG = {"shared-calendar": PAY,   # payroll dates, listed under Start Here
            "change-salary": PAY}    # a pay topic, listed under Assignment Changes since the SME review

def owner(c):
    """The team that owns a course: Payroll for payroll and financial topics, HRIS for everything else."""
    return _BY_SLUG.get(c["slug"]) or _BY_TOPIC.get(c["topic"], HIRE)

# How the V.02 draft first showed the owner on Nov 12, kept so the change log stays true. None = it had no owner yet.
_FIRST_BY_TOPIC = {"payroll": "Payroll and Finance", "costing": "Payroll and Finance", "recruiting": "Recruiting and Hiring", "students": "Recruiting and Hiring"}
_FIRST_BY_SLUG = {"shared-calendar": "Payroll and Finance", "i9-background-by-worker-type": "Recruiting and Hiring", "student-faculty-changes": None}

def owner_first(c):
    s = c["slug"]
    return _FIRST_BY_SLUG[s] if s in _FIRST_BY_SLUG else _FIRST_BY_TOPIC.get(c["topic"])

# ───────────── Cutoffs ─────────────
PENDING = "Pending approvals do not pay. A change still waiting in approvals at the cutoff misses that payroll."
CUTOFF = {
    "monthly": "Monthly (exempt) pay: the change must be fully approved by the HCM Transaction Cutoff, the 18th in most months and earlier in December. Check the HR/Payroll Calendar. " + PENDING,
    "hire": "No pay starts until the hire is approved. Check the payroll calendar for the cutoff that applies to the person's pay cycle. " + PENDING,
    "time": "Weekly and biweekly pay: time cards are due at noon on the Monday after the pay period ends, and holiday weeks move that. Check the HR/Payroll Calendar. After payroll signs off, an approval can't be removed unless payroll removes the sign-off first.",
    "term": "Submit before the HCM Transaction Cutoff so pay stops on time. For monthly pay it is the 18th in most months; check the HR/Payroll Calendar.",
    "costing": "Current and future changes: enter by the HCM Transaction Cutoff. Prior periods: send the Retro Costing Request Form (Salary) to the Research Finance Team by the Retro Change Cutoff, usually two business days earlier.",
    "position": "No payroll cutoff applies to a position. It must be approved and active before it can be posted or used, so date it today.",
    "offcycle": "Off-cycle runs are on the HR/Payroll Calendar, with a cutoff of noon two days before each one. Payroll can't run the off-cycle payment until the Oracle transaction is approved. If the request does not meet the criteria on the form, the amount pays in the next regular payroll.",
    "leave": "To confirm: how leave entries line up with the payroll cutoffs. Vanderbilt's leave process is pending review by the Leave SME.",
}

# One-line versions for the printed job aid and the Playbook.
CUTOFF_SHORT = {
    "monthly": "Fully approved by the HCM Transaction Cutoff (the 18th in most months, earlier in December). Pending approvals do not pay.",
    "hire": "Approved before the cutoff for the person's pay cycle. No approval, no pay.",
    "time": "Due at noon on the Monday after the pay period ends. Holiday weeks move it.",
    "term": "Submitted before the HCM Transaction Cutoff, so pay stops on time.",
    "costing": "By the HCM Transaction Cutoff. Prior periods: the retro form by the Retro Change Cutoff, usually two business days earlier.",
    "position": "No payroll cutoff. Date it today so it can be used.",
    "offcycle": "Noon two days before the off-cycle run, and only once the Oracle transaction is approved.",
    "leave": "To confirm with the Leave SME.",
}

# The check every pay-impacting transaction gets, from the Data integrity course.
STANDARD_CHECK = "Read every field back against the source document: person, effective date, position, hours, pay, and costing."
CHAIN = "To confirm: the approval chain for this transaction."

# ───────────── Before you submit ─────────────
# tx       the transaction, as HCMs name it
# docs     (document, status). Status is what the course says today:
#          "Required" the course says it is needed; "Attach" the course tells you to attach or file it;
#          "If finance asks" the course leaves it to the finance approver.
# docs_gap what the course does not say yet about documents (shown as "To confirm")
# confirm  any other point the owner still has to confirm (shown as "To confirm")
# checks   the checks that matter most for this transaction, from the course's own steps and watch-outs
# cutoff   a key in CUTOFF
# submits / approves / then   who does what
# title    the block's heading when "Before you submit" does not fit (time cards are approved or saved)
# standard False when the read-back check against a source document does not apply
BEFORE = {
 "create-position": dict(tx="Create a position",
    docs=[("Pre-search memo from Compensation", "Required"), ("Approved position description", "Attach")],
    checks=["Effective date is today, not the start date.",
            "The six-digit job code and assignment category match the memo.",
            "Location is where the person would sit on site.",
            "Standard working hours stay at 40. Working hours hold the actual hours."],
    cutoff="position", submits="You", approves=CHAIN, then="Once approved, the position can go on a requisition. The hire inherits from it."),
 "update-position": dict(tx="Update a position (including a reclassification)",
    docs=[("Reclass memo from Compensation, for a reclassification", "Required")],
    docs_gap="What to attach for a position update that is not a reclassification.",
    checks=["The action reason matches the change.",
            "The new job code, name, and assignment category match the reclass memo.",
            "After approval, update the incumbent's assignment for what does not flow: person type, location, working hours, and hourly salary."],
    cutoff="position", submits="You", approves=CHAIN, then="Position changes never reach an existing requisition. Update the incumbent's assignment yourself."),
 "create-requisition": dict(tx="Create a requisition",
    docs=[("Pre-search memo from the last 12 months, with a job code that matches the position", "Required"), ("Position description", "Attach")],
    checks=["The position is right before you start. The requisition copies it when submitted.",
            "Openings are a number, never Unlimited.",
            "Location is a real work location, never United States.",
            "New York: the New York candidate selection process and account VAN09."],
    cutoff=None, submits="You", approves="More than one opening also goes to central finance. " + CHAIN,
    then="Recruiting works the requisition. The recruiter makes the offer."),
 "convert-pending-worker": dict(tx="Convert a pending worker (hire)",
    docs=[("Offer letter, for your business unit approver", "Attach")],
    docs_gap="The exact payroll elements to confirm at hire are still being documented with the payroll team.",
    checks=["Action Hire, reason Employment. The other reasons are for students on a stipend and for affiliates.",
            "Business unit and position match the offer.",
            "Assignment status is Active payroll eligible for anyone who is paid.",
            "Payroll details and salary show what the person will actually be paid.",
            "Location is where the person will actually work."],
    cutoff="hire", submits="You, after the clear to start email", approves="Your business unit approver.",
    then="Payroll pays what the record says. A missing element or a wrong conversion means a wrong first paycheck."),
 "change-assignment": dict(tx="Change Assignment",
    docs=[], docs_gap="No document is named for this transaction yet.",
    checks=["It is not a move to another position. That is a transfer.",
            "The effective date lines up with the payroll calendar.",
            "Salary is selected and reviewed if the change affects pay.",
            "After a reclassification: person type, location, working hours, and hourly salary are updated here."],
    cutoff="monthly", submits="You", approves=CHAIN, then="Payroll pays from the approved assignment."),
 "change-working-hours": dict(tx="Change working hours",
    docs=[("The approval or agreement for the change", "Attach")],
    checks=["You are in Change Assignment with Salary selected, so hours and pay change together.",
            "Working hours hold the new weekly hours. Standard working hours stay at 40.",
            "FTE recalculated as expected (for example, 30 of 40 = 0.75).",
            "Salary is prorated, or the agreed amount is entered."],
    cutoff="monthly", submits="You", approves=CHAIN, then="Payroll pays the new salary from the effective date."),
 "promote": dict(tx="Promote (no requisition)",
    docs=[], docs_gap="No document is named yet, and whether Compensation must approve the new salary is an open item.",
    checks=["Who processes it: from a requisition, PCB Internal Talent Acquisition. With no requisition, you.",
            "The target position exists with the correct six-digit job code.",
            "The Salary step is on and the new salary is entered.",
            "After a position change: person type, location, working hours, and hourly salary are checked on the assignment."],
    cutoff="monthly", submits="You, when there is no requisition", approves=CHAIN, then="Payroll pays the new salary from the effective date."),
 "transfer-without-requisition": dict(tx="Transfer or promotion without a requisition",
    docs=[], docs_gap="No document is named for this transaction yet.",
    checks=["It did not come from a job application. Those go to central HR.",
            "The effective date lines up with payroll.",
            "Extra sections are selected if pay changes.",
            "Costing is reviewed. Existing costing follows the employee and does not reset."],
    cutoff="monthly", submits="You", approves=CHAIN, then="You review costing in the new area. Payroll pays from the approved assignment."),
 "add-assignment": dict(tx="Add an assignment (second job)",
    docs=[], docs_gap="No document is named yet, and whether a second assignment needs pre-approval from Compensation or your PCB consultant is an open item.",
    checks=["The person already has an active employee assignment.",
            "The position for the new job exists and is correct.",
            "Only one assignment is primary.",
            "Salary, payroll details, and costing are entered for the new assignment."],
    cutoff="monthly", submits="You", approves=CHAIN, then="Each assignment has its own costing, hours, and pay."),
 "change-salary": dict(tx="Change salary",
    docs=[("Signed letter (for example, a retention letter), filed as a Compensation Letters document record", "Attach"),
          ("Comments and attachments your finance approver expects", "If finance asks")],
    docs_gap="Which salary change reasons require which document.",
    checks=["The effective date is when the new salary starts.",
            "The reason matches the change. Annual increase and union reasons are not for off-cycle changes.",
            "The new amount or percentage is right.",
            "Hours changing too? Use Change Assignment with Salary selected."],
    cutoff="monthly", submits="You", approves="Many departmental finance approvers review these. " + CHAIN,
    then="Payroll picks up the approved salary in the payroll period it falls in. A backdated change pays later as retro."),
 "staff-supplement": dict(tx="Add a staff supplement",
    docs=[("Interim pay letter, filed as a Compensation Letters document record", "If finance asks")],
    docs_gap="Whether the letter is required for every supplement.",
    checks=["The plan is the supplement your FUM asked for.",
            "The amount is per payroll, and it is filled in.",
            "Start date is the first day of the target payroll month.",
            "An end date is set, or Ongoing is on with a reminder to end it."],
    cutoff="monthly", submits="You", approves=CHAIN, then="It pays every payroll until it ends. Someone has to end an ongoing supplement."),
 "sign-on-bonus": dict(tx="Add a one-time payment (such as a sign-on bonus)",
    docs=[("Offer or bonus letter; the signed letter filed as a Compensation Letters document record", "If finance asks")],
    docs_gap="Whether the letter is required for every one-time payment.",
    checks=["It is not already on the offer. Adding it to the offer is the preferred path.",
            "The amount is in Amount, not Net. Amount is gross.",
            "Start date is the first day of the target payroll month.",
            "Process separately is left at Yes."],
    cutoff="monthly", submits="You. For a new hire, the recruiter normally adds it to the offer", approves=CHAIN,
    then="It pays with the regular paycheck for that month."),
 "net-one-time-stipend": dict(tx="Grossed-up additional compensation (net payment)",
    docs=[("The manager's request (email or memo), saying what the payment is for", "Attach")],
    checks=["Plan is Lump sum payment.",
            "The amount is in Net, not Amount. Net is take-home.",
            "Start date is the first day of the target payroll month. Past the cutoff, date it for next month.",
            "Process separately is left at Yes unless payroll tells you otherwise."],
    cutoff="monthly", submits="You", approves=CHAIN, then="Oracle works out the gross. Pay goes to direct deposit."),
 "off-cycle-payment": dict(tx="Request an off-cycle payment",
    docs=[("The off-cycle paycheck request form", "Required")],
    checks=["The Oracle transaction is submitted or resubmitted first.",
            "The request meets the criteria shown on the form.",
            "The reason matches what went wrong.",
            "Payroll has the employee's name and ID, and when the transaction will be approved."],
    cutoff="offcycle", submits="You: the Oracle transaction and the form", approves="Payroll decides whether the request qualifies.",
    then="Payroll runs the payment and you tell the employee when to expect it."),
 "review-approve-time-cards": dict(tx="Approve a time card", title="Before you approve", standard=False,
    docs=[], docs_none="None. The approved time card is the record.",
    checks=["Exceptions such as a missing punch are resolved before you approve.",
            "You are in the completed pay period, not the open one.",
            "Hours and pay codes match what the employee worked.",
            "You did not submit this time card yourself. The person who submits a time card does not approve it."],
    confirm="Payroll to confirm the rule on who approves, and who approves when the manager is out.",
    cutoff="time", submits="The employee approves their own time card first", approves="The manager approves. Payroll signs off.",
    then="Payroll pays the approved hours."),
 "enter-pto": dict(tx="Enter PTO on a time card", title="Before you save", standard=False,
    docs=[], docs_none="None. The time card is the record.",
    checks=["The pay code matches what the employee requested.",
            "The PTO is on a new row for the day, not on a row with a punch.",
            "Open period: Save only. Do not submit.",
            "You reopened the time card and the entry saved."],
    cutoff="time", submits="You, when the employee can't enter it", approves="The manager approves the time card. Payroll signs off.",
    then="Payroll pays the PTO hours with the time card."),
 "voluntary-termination": dict(tx="Voluntary termination",
    docs=[], docs_gap="No document is named yet. Confirm whether the resignation notice is filed and where.",
    checks=["Notification date is the day they told you. Termination date is their last day.",
            "Other assignments are checked. End only yours if they keep one.",
            "Direct reports are moved to a new manager before the termination date.",
            "Payroll eligibility is left as defaulted.",
            "Non-exempt: the final time card is approved."],
    cutoff="term", submits="You", approves=CHAIN, then="The termination stops pay and Oracle notifies payroll. Do not send a separate payroll request."),
 "involuntary-termination": dict(tx="Involuntary termination (misconduct)",
    docs=[], docs_gap="No document is named yet. Confirm with your PCB consultant what is filed and where.",
    checks=["Your PCB consultant and department leadership are consulted first.",
            "Access timing and the rehire field are settled before you start.",
            "Notification date and termination date are right, usually today.",
            "Direct reports and other assignments are checked."],
    cutoff="term", submits="You, after your PCB consultant and leadership agree", approves=CHAIN,
    then="The termination stops pay and Oracle notifies payroll."),
 "reduction-in-force": dict(tx="Reduction in force",
    docs=[], docs_gap="The separation agreement drives the dates. Confirm whether it is attached or filed.",
    checks=["Termination date is the end of the 60-day notice.",
            "Last working day follows the scenario in the separation agreement.",
            "Payroll eligibility is left as defaulted.",
            "Separation pay is paid separately with its own element."],
    cutoff="term", submits="You", approves=CHAIN, then="Regular pay runs to the termination date. Separation pay set by the agreement is paid separately."),
 "terminate-multiple-assignments": dict(tx="Termination with more than one assignment",
    docs=[], docs_gap="No document is named yet, and who submits when the jobs sit in different business units is an open item.",
    checks=["Every active assignment is listed and the primary one is found.",
            "Leaving all jobs is Terminate Employment. Leaving only yours is End Assignment.",
            "The HCM who owns the other assignment knows.",
            "Primary is changed first if your job is primary and they keep another."],
    cutoff="term", submits="You, with the other assignment's HCM", approves=CHAIN,
    then="Terminate Employment stops pay for every job. End Assignment stops only yours."),
 "enter-edit-costing": dict(tx="Enter costing for a person",
    docs=[("Prior periods: the Retro Costing Request Form (Salary), sent to the Research Finance Team", "Required"),
          ("Cost transfer memo, if an externally funded grant is affected", "Required")],
    checks=["Effective As-of Date is the first day of the pay period the costing should start.",
            "The lines total 100%.",
            "The COA or POET string came from your FUM.",
            "You ran the HCM Cost Allocation Verification Plan report afterward."],
    confirm="Where the Retro Change Cutoff is published. It is not on the HR/Payroll Calendar.",
    cutoff="costing", submits="You. Entering costing needs the HCM role in Oracle; get the costing string from your FUM", approves=CHAIN,
    then="Oracle uses the costing in effect on the Pay Period End Date and does not prorate."),
 "change-existing-costing": dict(tx="Change existing costing",
    docs=[("Prior periods: the Retro Costing Request Form (Salary), sent to the Research Finance Team", "Required"),
          ("Cost transfer memo, if an externally funded grant is affected", "Required")],
    checks=["You reviewed History before the change.",
            "The action is right: Update, Correct, End Date, or Delete Record.",
            "End Date ends everything from that date forward.",
            "The lines total 100%, and you ran the verification report afterward."],
    confirm="Where the Retro Change Cutoff is published. It is not on the HR/Payroll Calendar.",
    cutoff="costing", submits="You. Entering costing needs the HCM role in Oracle; get the costing string from your FUM", approves=CHAIN,
    then="Costing results post to the General Ledger after payroll runs."),
 "fmla-tmla-transactions": dict(tx="FMLA or TMLA absence",
    docs=[("Supporting documents, if the absence type asks for them", "Attach")],
    docs_gap="Which absence types Vanderbilt uses, who enters intermittent occurrences, and where leave approval letters are stored (outside Oracle Document Records).",
    checks=["The absence type matches the approval.",
            "Continuous leave: one absence with the approved start and end dates.",
            "Intermittent or reduced schedule: only the time actually taken."],
    cutoff="leave", submits="You. To confirm: who enters intermittent occurrences", approves="To confirm: the approval routing for each absence type.",
    then="To confirm: how the leave reaches pay."),
 "student-faculty-changes": dict(tx="Student and faculty assignment changes",
    docs=[], docs_gap="No document is named for these changes yet.",
    checks=["A move to another position is a transfer, not Change Assignment.",
            "An assignment that ends at term end is ended, not left open.",
            "Costing and the fields that do not flow from the position are reviewed."],
    cutoff="monthly", submits="You. From a requisition, PCB Internal Talent Acquisition processes it", approves=CHAIN,
    then="An assignment left open past term end keeps the person active and payable."),
}

# Rows for the Who owns what table that are not a "Before you submit" transaction.
WHO_EXTRA = [
    ("Job code and level for a role", "Compensation picks the job. You do not.", "Compensation, through the pre-search or reclass memo.", "None."),
    ("Exempt or non-exempt status", "Do not decide it yourself.", "Compensation.", "Payroll pays by the status on the record."),
    ("Background check", "You set it up on the requisition and wait for clearance.", "The background check team clears the hire.", "None."),
    ("Transfer or promotion from a requisition", "Not you. Never create a direct hire for someone already in process.", "Recruiting sends it to central HR, which processes it.", "Payroll pays from the approved assignment."),
    ("Weekly time card check", "You, every week. You chase managers for missing or late time cards.", "Employees and managers approve.", "Payroll signs off, then runs payroll."),
    ("A pay error", "You bring the facts: what was expected, what was paid, what the record shows.", "The manager helps with time card facts.", "Payroll decides how and when to correct it, including any off-cycle payment."),
    ("Running payroll", "Never you. Do not try to run or rerun payroll.", "None.", "Payroll."),
]

# courses merged by the SME review keep the block of the course they absorbed
BEFORE_ALIAS = {"ukg-time-cards": "review-approve-time-cards", "end-assignment-vs-terminate": "terminate-multiple-assignments"}

def before(slug):
    return BEFORE.get(slug) or BEFORE.get(BEFORE_ALIAS.get(slug, ""))

def has_before(slug):
    return before(slug) is not None

def sentence(s):
    return s if s.endswith(".") else s + "."

def attach_line(b):
    """What to attach, in one line, for the printed job aid and the Playbook."""
    if b.get("docs_none"): return b["docs_none"]
    line = " ".join(f"{d} ({st.lower()})." for d, st in b["docs"]) or "None named yet."
    return line + (f" To confirm: {b['docs_gap']}" if b.get("docs_gap") else "")

def docs_rows():
    """Rows for the What to attach table: transaction, what to attach or file, status today."""
    rows = []
    for b in BEFORE.values():
        if b.get("docs_none"):
            rows.append([b["tx"], b["docs_none"], "Not needed"]); continue
        for d, st in b["docs"]:
            rows.append([b["tx"], d, st])
        if not b["docs"]:
            rows.append([b["tx"], "None named yet", "To confirm"])
    return rows

def who_rows():
    """Rows for the Who owns what table: the work, your part, who else acts, payroll's part."""
    rows = [[b["tx"], sentence(b["submits"]), b["approves"], b["then"]] for b in BEFORE.values()]
    return rows + [list(r) for r in WHO_EXTRA]

# ───────────── Change log ─────────────
NEW_IN_V02 = {"what-to-attach", "who-owns-what", "shared-calendar", "pay-rules", "common-pay-errors"}
TIME_CARD_RULE = {"weekly-time-card-check", "ukg-time-cards"}
_VIDEO = "Added a narrated video and a detailed job aid with a picture for each step."
_TERMS = "Title now says Oracle HCM: in HCM Academy, HCM means the role, and Oracle HCM is the system."
_TERMS_DATA = "Wording: says Oracle HCM data where it means the system. In HCM Academy, HCM means the role."
_ORACLE = "Video and job aid rebuilt on the Oracle screens, from Oracle's documentation; steps outside Oracle stay as cards."
EXTRA_CHANGES = {
    # slug: [(date, text)] for hand-written entries. Newest first.
    "direct-reports": [(SCREENS, "Steps now follow Vanderbilt's Our Workforce screens: open Direct Reports from Show More, then search for the manager. " + _VIDEO)],
    "create-requisition": [(SCREENS, "Path corrected from Vanderbilt's Our Workforce screens: Hiring > Job Requisitions, or the Create Job Requisition quick action. " + _VIDEO)],
    "hire-non-worker": [(SCREENS, "Added an open item: when to use Add a Nonworker or Add a Contingent Worker, which Vanderbilt's Our Workforce screens list under New Person. " + _VIDEO)],
    "compensation-memo": [(SCREENS, _VIDEO)], "hire-staff": [(SCREENS, _VIDEO)],
    "background-checks": [(REVIEWED_ON, _ORACLE), (SCREENS, _VIDEO)],
    "executive-search": [(REVIEWED_ON, _ORACLE), (SCREENS, _VIDEO)],
    "create-position": [(SCREENS, _VIDEO)], "update-position": [(SCREENS, _VIDEO)], "convert-pending-worker": [(SCREENS, _VIDEO)],
    "hcm-structure": [(REVIEWED_ON, _TERMS + " " + _VIDEO)], "workflow-worklists": [(REVIEWED_ON, _TERMS + " " + _VIDEO)],
    "who-owns-what": [(REVIEWED_ON, _VIDEO)], "quick-actions-person-info": [(REVIEWED_ON, _VIDEO)], "shared-calendar": [(REVIEWED_ON, _VIDEO)],
    "ferpa-for-staff": [(REVIEWED_ON, _VIDEO)], "i9-background-by-worker-type": [(REVIEWED_ON, _VIDEO)], "employee-vs-contractor": [(REVIEWED_ON, _VIDEO)],
    "data-integrity": [(REVIEWED_ON, "Watch-out matched to the SME review of Position best practices: reuse an inactive position only if it meets current guidelines. " + _VIDEO)],
    "bi-intro-playbook": [(REVIEWED_ON, _TERMS_DATA)], "reporting-101": [(REVIEWED_ON, _TERMS_DATA)], "reporting-301": [(REVIEWED_ON, _TERMS_DATA)],
    "rehire-eligibility": [(REVIEWED_ON, _ORACLE + " Field names in steps 1 and 2 now follow Oracle's documentation: Recommended for Rehire (Yes, No, Not Specified), and the search option to include terminated work relationships."), (SCREENS, _VIDEO)],
}

EXTRA_CHANGES["ukg-time-cards"] = [(REVIEWED_ON, "Video and job aid rebuilt from Vanderbilt's recorded UKG walkthrough, with fictional names. They replace the "
    "Guidde video and its blurred screenshots. The PTO-Vacation and PTO-Sick pay codes are confirmed on screen.")] + EXTRA_CHANGES.get("ukg-time-cards", [])
_FUM = "Wording: says FUM (financial unit manager), Vanderbilt's term, where it said finance partner."
for _s in ("change-salary", "sign-on-bonus", "staff-supplement", "costing-impacts", "what-to-attach", "enter-edit-costing"):
    EXTRA_CHANGES[_s] = [(REVIEWED_ON, _FUM)] + EXTRA_CHANGES.get(_s, [])

# Changes made on Nov 13, 2026 from Vanderbilt's own published pages: the HR/Payroll Calendar for 2026 and 2027
# (People Experience, Pay Calendar page) and the Vanderbilt Student Privacy Statement (University Registrar).
_MONTHLY_FIX = "Monthly cutoff corrected from the published HR/Payroll Calendar: the 18th in most months, earlier in December."
_TIME_FIX = "Added when time cards are due, from the published HR/Payroll Calendar: noon on the Monday after the pay period ends."
PUBLISHED = {
    "shared-calendar": "Rewritten from Vanderbilt's published HR/Payroll Calendar for 2026 and 2027: where it is, each cutoff, when time cards are due, and off-cycle runs.",
    "ferpa-for-staff": "Added Vanderbilt's directory information list and the University Registrar as the contact, from the Vanderbilt Student Privacy Statement.",
    "comp-impacts-payroll": "Cutoffs corrected from the published HR/Payroll Calendar: the 18th in most months for monthly pay, and the Friday a week before payday for weekly and biweekly pay.",
    "exempt-time-off": _MONTHLY_FIX, "change-salary": _MONTHLY_FIX,
    "weekly-time-card-check": _TIME_FIX, "ukg-for-managers": _TIME_FIX,
    "off-cycle-payment": "Added the off-cycle schedule from the published HR/Payroll Calendar: noon, two days before each run.",
    "hire-staff": "Course names corrected to match the catalog.",
    "pay-rules": "Added the pay period days from the published HR/Payroll Calendar to the open item on the workweek.",
}
_BLOCK_FIX = "Cutoff in Before you submit updated from the published HR/Payroll Calendar."

def fold_items(items):
    """Drop an open item when most of its words are already in a longer item for the same course, so reviewers answer each point once."""
    import re
    stop = set("the a an of to in is it and or for on at by you your with that this be are as from not do does can if then than they their its who what which whether how when where confirm vanderbilt vanderbilt's exact each any must still yet".split())
    toks = lambda s: {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in stop and len(w) > 2}
    keep = []
    for text in sorted(items, key=lambda x: -len(x)):
        t = toks(text)
        if any(len(t & toks(k)) >= 0.6 * max(1, len(t)) for k in keep): continue
        keep.append(text)
    return [x for x in items if x in keep]

def changes(c):
    """What changed on a course, newest first: (date, text)."""
    import reviews
    s = c["slug"]
    import restructure
    if s in reviews.NEW: return list(EXTRA_CHANGES.get(s, [])) + ([(REVIEWED_ON, restructure.NOTES[s])] if s in restructure.NOTES else []) + \
        [(REVIEWED_ON, reviews.NOTES.get(s, "New course."))]
    if s == restructure.ROLE["slug"]: return [(REVIEWED_ON, restructure.NOTE)]
    own = owner(c); was = owner_first(c); out = ([(REVIEWED_ON, restructure.NOTES[s])] if s in restructure.NOTES else []) + \
        ([(REVIEWED_ON, reviews.NOTES[s])] if s in reviews.NOTES else []) + list(EXTRA_CHANGES.get(s, []))
    b = before(s)
    if s in PUBLISHED: out.append((OWNERS_SET, PUBLISHED[s] + (" " + _BLOCK_FIX if b and b.get("cutoff") in ("monthly", "term", "time", "offcycle") else "")))
    elif b and b.get("cutoff") in ("monthly", "term", "time", "offcycle"): out.append((OWNERS_SET, _BLOCK_FIX))
    out.append((OWNERS_SET, f"Owner is now {own}. " + (f"It was shown as {was}." if was else "It had no owner yet.")))
    if s in NEW_IN_V02:
        out.append((UPDATED, "New course."))
        return out
    bits = []
    if s in BEFORE: bits.append("Added Before you submit: what to attach, what to check, the cutoff, and who does what.")
    if s in TIME_CARD_RULE: bits.append("Added the rule that the person who submits a time card does not approve it.")
    bits.append(f"Owner shown: {was}." if was else "Owner still to be named.")
    out.append((UPDATED, " ".join(bits)))
    out.append((FIRST, "First draft (V.01)."))
    return out

def updated(c):
    """The date of a course's newest change."""
    return changes(c)[0][0]
