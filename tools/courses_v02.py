# Courses added in V.02: what to attach, who owns what, pay rules, common pay errors, and the HR/Payroll calendar.
# Same shape as the courses in tools/course_content.py. Two of them are tables built from
# tools/governance.py, so the table and the "Before you submit" block on each course never disagree.
# Rules: no em or en dashes; every fact comes from another HCM Academy course or an official source;
# anything Vanderbilt has not confirmed is an open item, not a guess.
import governance as G

DOL = "https://www.dol.gov/"
_COURSES_NOTE = "Built from the other HCM Academy courses. Not yet confirmed by the course owners; confirm the open items before release."

def build(BY):
    """New courses. BY maps slug to course, so each one can name the courses it draws on."""
    n = lambda slug: BY[slug]["name"]
    return [
    # ───────────── What to attach ─────────────
    dict(slug="what-to-attach", topic="records", topic_label="Document Records & Reporting",
     title_pre="Know what to", title_em="attach", name="What to attach: documents by transaction",
     system="Overview", time="5 min",
     sources=["HCM Academy courses for each transaction (named in the table)", "Personnel Files: Document Records, Oracle User Guide"],
     intro=["Approvers send transactions back when the supporting document is missing, and payroll can only trust a change it can trace to a signed source. This course puts what every course says about documents into one table.",
            "It is a draft. Where a course does not name a document yet, the table says so, and the owner for that area will confirm what is required."],
     use_when="You are about to submit a hire, a pay change, a termination, or a costing change and want to know what goes with it.",
     steps_title="How to use the table",
     steps=[
      {"t": "Find your transaction in the table.", "d": "The table lists each pay-impacting transaction, the document its course names, and the status of that document today."},
      {"t": "Read the status.", "d": "The status is what the course says now. It is not yet one confirmed standard for every area.",
       "sub": ["Required: the course says you need it.", "Attach: the course tells you to attach or file it.", "If finance asks: your finance approver decides.", "To confirm: no document is named yet."]},
      {"t": "Get the final, signed copy before you start.", "d": "Document records hold final, signed copies only. A draft or an unsigned letter is not the record."},
      {"t": "Attach it to the transaction, and file it when the course says so.", "d": f"Letters about pay go on the employee's file as a Compensation Letters document record. Leave and accommodation records are stored outside Oracle Document Records. See {n('add-document-record')} for the steps and the naming convention."},
      {"t": "Say what the change is for in the comments.", "d": "A short note on what is changing and why saves a send-back. Oracle needs little in comments and attachments, but many departmental finance approvers want more."},
      {"t": "When the table says To confirm, ask before you submit.", "d": "Ask your FUM or your PCB consultant what they expect. Tell the course owner what you learn, so the table can be completed."},
     ],
     table=dict(title="What to attach, by transaction (draft)", head=["Transaction", "Attach or file", "Status today"], rows=G.docs_rows(), tight_last=True),
     watch=["Required means the course says so. The owners have not yet confirmed one standard for every area.",
            "File final, signed copies only.",
            "Open item: for each transaction, owners to confirm which documents are required and which are optional."],
     docs=[("Oracle: Overview of Document Records", "https://docs.oracle.com/en/cloud/saas/human-resources/faigh/overview-of-document-records.html")],
     quiz=[
      dict(q="The table shows To confirm for your transaction. What do you do?", o=["Submit with no attachment and no comment", "Ask your FUM or PCB consultant what they expect", "Attach every document in the employee's file"], a=1, why="To confirm means no standard is set yet. Ask before you submit, and tell the course owner what you learn."),
      dict(q="Where does a signed retention letter go?", o=["A Compensation Letters document record on the employee's file", "A folder on your own shared drive", "The comments box, typed out by hand"], a=0, why="Letters about pay are filed as Compensation Letters document records."),
      dict(q="Which copy of a document do you file?", o=["The first draft, so the date is early", "The final, signed copy", "Any copy, as long as it is dated"], a=1, why="Document records hold final, signed copies only."),
     ],
     pending=_COURSES_NOTE),

    # ───────────── Who owns what ─────────────
    dict(slug="who-owns-what", topic="start", topic_label="Start Here",
     title_pre="Know who owns", title_em="what", name="Who owns what: your part, by transaction",
     system="Overview", time="5 min",
     sources=["HCM Academy courses for each transaction (named in the table)", "Payroll SME session, Oct 19"],
     intro=["Many pay problems are handoff problems: each person assumed someone else had it. This course shows, for each transaction, what you do, who else acts, and what happens next.",
            "It is a draft. Approval chains by transaction type are not confirmed yet, so those cells say To confirm."],
     use_when="You are not sure whether a step is yours, who acts after you, or who to go to when something is wrong.",
     steps_title="How the work is split",
     steps=[
      {"t": "You own the record.", "d": "You enter hires, changes, and terminations for your area, and you check time cards every week. Payroll can only pay what the record says."},
      {"t": "Compensation owns the job behind the pay.", "d": "Compensation picks the job code and level and issues the pre-search and reclass memos. Do not decide exempt or non-exempt status yourself."},
      {"t": "Recruiting and central HR own moves that come from a requisition.", "d": "A transfer or promotion that came from a job application is processed by central HR. Do not submit it yourself."},
      {"t": "Employees and managers own the hours.", "d": "The employee approves their time card, the manager approves it, and payroll signs off. You check that nothing is stuck."},
      {"t": "FUMs own the funding.", "d": "Get the costing string from your FUM (financial unit manager). In many areas the FUM also enters costing, so confirm who owns it in your department."},
      {"t": "Payroll owns the payroll run and every correction.", "d": "Bring payroll the facts: what was expected, what was paid, and what the record shows. Payroll decides how and when to correct the pay."},
      {"t": "Track your transaction until it is approved.", "d": "Check the notifications bell daily and before the cutoff. A transaction that is still pending does not pay."},
     ],
     table=dict(title="Who owns what, by transaction (draft)", head=["The work", "Your part", "Who else acts", "What happens next"], rows=G.who_rows()),
     watch=["Never try to run or rerun payroll yourself.",
            "Never create a direct hire for someone already in a recruiting process.",
            "Open item: approval chains by transaction type are not confirmed. The owners will fill in the cells that say To confirm."],
     docs=[("Oracle: Approval Management Configuration Options for Oracle Fusion Human Capital Management", "https://docs.oracle.com/en/cloud/saas/human-resources/24d/faucf/approval-management-configuration-options-for-oracle-fusion.html")],
     quiz=[
      dict(q="An employee's paycheck was short. What is your part?", o=["Rerun payroll for that one employee", "Bring payroll the facts and let payroll decide the correction", "Enter a one-time payment for the difference"], a=1, why="You bring the facts. Payroll decides how and when to correct the pay, including any off-cycle payment."),
      dict(q="A promotion came from a posted requisition. Who processes it?", o=["You, using the Promote action", "Central HR, through recruiting", "The employee's new manager"], a=1, why="Moves that come from a requisition are processed by central HR. You do not submit them."),
      dict(q="Who decides whether a role is exempt or non-exempt?", o=["You, from the job description", "The hiring manager", "Compensation"], a=2, why="Do not decide exemption yourself. Compensation does."),
     ],
     pending=_COURSES_NOTE),

    # ───────────── Pay rules ─────────────
    dict(slug="pay-rules", topic="payroll", topic_label="Payroll & Timecards",
     title_pre="Know the rules behind the", title_em="paycheck", name="Pay rules: overtime, holidays, shifts, and on-call",
     system="Overview", time="7 min",
     sources=["DOL: Fact Sheet #23, Overtime Pay Requirements of the FLSA", "DOL: Fact Sheet #22, Hours Worked Under the FLSA",
              "DOL: Fact Sheet #56A, Overview of the Regular Rate of Pay Under the FLSA", "DOL: Holiday Pay"],
     intro=["Non-exempt pay is built from hours and pay rules. When a rule is misread or a time card is coded wrong, the paycheck is wrong even though every punch is there.",
            "This draft covers the federal rules, which set the floor. Vanderbilt's own rules for holidays, shift differentials, and on-call pay are being documented by Payroll and are listed as open items."],
     use_when="A manager or employee asks how overtime, a holiday, a shift, or on-call time is paid, or a time card total looks wrong.",
     steps_title="The rules that change pay",
     steps=[
      {"t": "Start with who the rules apply to.", "d": "Weekly and biweekly (non-exempt) employees are paid from approved time cards, so these rules apply to them. Monthly (exempt) employees are paid a salary. Do not decide exempt or non-exempt status yourself; Compensation does."},
      {"t": "Overtime: more than 40 hours worked in a workweek.", "d": "Federal law requires at least one and one-half times the regular rate for hours worked over 40 in a workweek. It does not require overtime only because the work fell on a weekend, a holiday, or a day off.",
       "sub": ["Over 40 hours worked in the workweek: overtime.", "Weekend or holiday work by itself: not overtime under federal law."]},
      {"t": "Count each workweek on its own.", "d": "A workweek is a fixed, repeating period of seven days. Hours are not averaged across two weeks, even for an employee paid biweekly: 30 hours one week and 50 the next is 10 overtime hours."},
      {"t": "Count hours worked, not hours paid.", "d": "Under federal law, paid time that was not worked, such as PTO, a holiday, or sick time, does not count toward the 40 hours. An employer's own policy can be more generous."},
      {"t": "Holidays: paid by policy, not by federal law.", "d": "Federal law does not require pay for a holiday that is not worked, or extra pay for working one. Both come from the employer's policy, so the pay code on the time card matters."},
      {"t": "Shift differentials: paid by policy, and they raise the overtime rate.", "d": "Federal law does not require a shift differential. When one is paid, it is part of the regular rate, so overtime is figured on pay that includes it."},
      {"t": "On-call time: it depends on how free the employee is.", "d": "Tighter limits on what the employee can do while on call can make the time count as hours worked.",
       "sub": ["Required to stay at the work site: hours worked.", "At home and free to use the time: generally not hours worked.", "Called in to work: the time spent working counts."]},
      {"t": "Unapproved overtime still gets paid.", "d": "Work an employee was allowed to do counts as hours worked, even if no one asked for it. A manager handles unapproved overtime through scheduling and coaching, never by leaving the hours off the time card."},
      {"t": "Check the time card, then ask payroll.", "d": "In your weekly check, look at totals over 40, holiday weeks, and unusual pay codes. For how a rule applies at Vanderbilt, give payroll the employee, the pay period, and what the time card shows."},
     ],
     watch=["These are the federal rules. A state where the employee works can require more.",
            "Never remove or reduce hours an employee worked to avoid overtime.",
            "Open item: Vanderbilt's rule on whether paid time off and holidays count toward overtime, and which seven days make the overtime workweek. The published calendar shows weekly pay periods running Monday to Sunday and biweekly periods Sunday to Saturday.",
            "Open item: Vanderbilt's holiday pay rules, shift differential rates, on-call and call-back pay, and the UKG pay code for each. Payroll is documenting these."],
     docs=[("DOL: Fact Sheet #23, Overtime Pay Requirements of the FLSA", DOL + "agencies/whd/fact-sheets/23-flsa-overtime-pay"),
           ("DOL: Fact Sheet #22, Hours Worked Under the FLSA", DOL + "agencies/whd/fact-sheets/22-flsa-hours-worked"),
           ("DOL: Fact Sheet #56A, Overview of the Regular Rate of Pay Under the FLSA", DOL + "agencies/whd/fact-sheets/56a-regular-rate"),
           ("DOL: Holiday Pay", DOL + "general/topic/workhours/holidays")],
     quiz=[
      dict(q="A biweekly employee works 30 hours in week one and 50 in week two. How many overtime hours?", o=["None, because the two weeks total 80", "10, because each workweek stands alone", "20, because week two is 20 over week one"], a=1, why="Hours are not averaged across weeks. Week two has 10 hours over 40."),
      dict(q="An employee stayed late without approval and worked 3 extra hours. What happens to those hours?", o=["They are paid, and the manager addresses it separately", "They come off the time card", "They move to the next pay period"], a=0, why="Work an employee was allowed to do is hours worked and must be paid. The manager handles the approval issue separately."),
      dict(q="A manager asks whether working a holiday is automatically overtime. What do you say?", o=["Yes, federal law requires it", "Not under federal law. Holiday pay comes from policy, so check with payroll", "Only for employees paid monthly"], a=1, why="Federal law does not require extra pay for holiday work. Vanderbilt's holiday rules are an open item, so ask payroll."),
     ],
     pending="Built from U.S. Department of Labor sources. Not yet reviewed by a Vanderbilt SME; confirm the open items before release."),

    # ───────────── Common pay errors ─────────────
    dict(slug="common-pay-errors", topic="payroll", topic_label="Payroll & Timecards",
     title_pre="Catch the errors that reach", title_em="payroll", name="Common pay errors and how to avoid them",
     system="Overview", time="6 min",
     sources=["HCM Academy courses (each error names its course)", "Payroll SME session, Oct 19", "HCM SME walkthrough, Oct 20"],
     intro=["These are the errors the HCM Academy courses warn about most. Each one sends wrong or missing data to payroll.",
            "It is a draft. The list is not yet ranked by how often each error happens. Payroll will supply the errors it corrects most, and this course will be updated from that list on a schedule."],
     use_when="You want to check your own work against the errors that most often cause a late or wrong paycheck.",
     steps_title="Ten errors to catch",
     steps=[
      {"t": "A paid person set to Active no payroll.", "d": f"Active no payroll means no pay at all. Use it only for unpaid affiliates. Course: {n('convert-pending-worker')}."},
      {"t": "A change still pending at the cutoff.", "d": f"Pending approvals do not pay. Submit early and track the transaction with the notifications bell. Course: {n('comp-impacts-payroll')}."},
      {"t": "The wrong effective date.", "d": f"A wrong date pays someone too early or too late, or creates retro pay. Check dates as carefully as amounts. Course: {n('data-integrity')}."},
      {"t": "Amount and Net mixed up on a one-time payment.", "d": f"Amount is gross. Net is take-home. Using the wrong field changes what the employee receives. Courses: {n('sign-on-bonus')}; {n('net-one-time-stipend')}."},
      {"t": "A supplement that never ends.", "d": f"An ongoing supplement keeps paying until someone ends it. Set an end date, or set a reminder. Course: {n('staff-supplement')}."},
      {"t": "Hours changed without the salary, or the salary without the hours.", "d": f"Use Change Assignment with Salary selected, so both change in one transaction. Course: {n('change-working-hours')}."},
      {"t": "A missing or unapproved time card.", "d": f"A time card that isn't approved won't pay correctly. Run the weekly check and contact the manager before the deadline. Course: {n('weekly-time-card-check')}."},
      {"t": "Terminate Employment used when the person keeps another job.", "d": f"It stops pay for every job. Use End Assignment on yours. Course: {n('terminate-multiple-assignments')}."},
      {"t": "Costing left as it was after a move.", "d": f"Costing follows the employee and does not reset. Review it after a transfer, a team change, or a funding change. Course: {n('when-to-update-costing')}."},
      {"t": "A wrong value on a position.", "d": f"Position values flow to every person in the position. Fix the position before the requisition, and don't reactivate or repurpose an old one. Course: {n('position-best-practices')}."},
     ],
     watch=["Fixes after payroll runs become retro adjustments in a later payroll and may mean a late or incorrect paycheck.",
            "If you find one of these after payroll has run, bring payroll the facts. Do not try to correct the pay yourself.",
            "Open item: Payroll to supply the errors it corrects most often, with counts, so this list can be ranked and kept current."],
     docs=[("Oracle: Recalculate Payroll for Retroactive Changes", "https://docs.oracle.com/en/cloud/saas/human-resources/faagp/recalculate-payroll-for-retroactive-changes.html")],
     quiz=[
      dict(q="A new staff member's assignment status is Active no payroll. What happens on payday?", o=["They are paid as usual", "They are not paid at all", "They are paid half until it is fixed"], a=1, why="Active no payroll means no pay. Use it only for unpaid affiliates."),
      dict(q="You find a wrong effective date after payroll has run. What do you do?", o=["Bring payroll the facts and let payroll decide the correction", "Delete the transaction so it reverses", "Wait to see whether the employee notices"], a=0, why="After payroll runs, the fix is a retro adjustment. Payroll decides how and when to correct it."),
      dict(q="A supplement for a three-month interim role is left as Ongoing. What is the risk?", o=["It stops after one payroll", "It keeps paying until someone ends it", "It turns into base salary"], a=1, why="Ongoing supplements keep paying until someone ends them."),
     ],
     pending="Built from the other HCM Academy courses. Not yet ranked or confirmed by Payroll; confirm the open items before release."),
    # ───────────── The HR/Payroll Calendar (replaces the parked draft in tools/courses_researched.py) ─────────────
    # Every date rule here was read from Vanderbilt's published HR/Payroll Calendar PDFs for 2026 and 2027.
    dict(slug="shared-calendar", topic="start", topic_label="Start Here",
     title_pre="Work to the HR/Payroll", title_em="calendar", name="The Shared Administrative Calendar",
     system="Overview", time="5 min",
     sources=["Vanderbilt HR/Payroll Calendar, 2026 and 2027 (People Experience, Pay Calendar page)", "Oracle: Overview of Payroll Definitions", "Oracle: Recalculate Payroll for Retroactive Changes"],
     intro=["Payroll runs on fixed dates. A transaction has to be approved before its cutoff, and a time card has to be in by its deadline, or the pay waits for the next run.",
            "Vanderbilt publishes those dates in the HR/Payroll Calendar. This course shows where it is and how to read it."],
     use_when="You are planning when to submit a transaction, or you need to know whether a change will make this payroll.",
     steps_title="How to read the calendar",
     steps=[
      {"t": "Open the HR/Payroll Calendar.", "d": "People Experience publishes it on the Pay Calendar page of its site (hr.vanderbilt.edu, under Payroll). There is one PDF for each year, with a page for each month. The 2026 and 2027 calendars are posted."},
      {"t": "Find your pay group.", "d": "Each row is one payroll. For each, the calendar gives the pay period, the paycheck date, the HCM Transaction Cutoff, and when time cards are due.",
       "sub": ["Weekly: Monday to Sunday.", "Biweekly: two weeks, Sunday to Saturday.", "Monthly: the calendar month.", "Academic Monthly: the 16th to the 15th.", "Off Cycle: extra runs, about two a month."]},
      {"t": "Monthly pay: the cutoff is the 18th in most months.", "d": "In 2026 the HCM Transaction Cutoff for monthly and academic monthly pay is the 18th in every month but December, when it is the 16th. It stays the 18th even when that is a weekend, so finish on the last working day before it. In 2027 it is the 17th or the 19th in five months."},
      {"t": "Weekly and biweekly pay: the cutoff is the Friday a week before payday.", "d": "The HCM Transaction Cutoff falls seven days before the paycheck date in nearly every pay period. Holiday weeks move it."},
      {"t": "Time cards are due at noon on the Monday after the pay period ends.", "d": "This is the Time Card Due column for weekly and biweekly pay. In holiday weeks the deadline moves, often to 10am or to Tuesday. Monthly pay has no time card."},
      {"t": "Off-cycle runs: noon, two days before.", "d": "The calendar lists the off-cycle paycheck dates. For each one, the HCM Transaction Cutoff and the time card deadline are noon two days before, usually a Wednesday."},
      {"t": "Submit early enough for approvals.", "d": "A transaction counts only once it is fully approved. Leave time for every approver to act before the cutoff, and track it with the notifications bell."},
      {"t": "Know what happens if you miss it.", "d": "A change that arrives after payroll is calculated is picked up as a retroactive adjustment in a later run. The person may be paid late or need a correction."},
     ],
     table=dict(title="The deadlines on the 2026 calendar", head=["Payroll", "Paid", "HCM Transaction Cutoff", "Time Card Due"], rows=[
      ["Weekly", "The Friday after the pay period ends", "The Friday a week before payday", "Noon on the Monday after the period ends"],
      ["Biweekly", "The Friday after the pay period ends", "The Friday a week before payday", "Noon on the Monday after the period ends"],
      ["Monthly and Academic Monthly", "The last business day of the month", "The 18th; December 16", "None"],
      ["Off Cycle", "About twice a month", "Noon, two days before the paycheck date", "Noon, two days before the paycheck date"]]),
     watch=["Do not work from memory. Dates move around holidays, and the December cutoff is early.",
            "Pending approvals do not pay. A change still waiting in approvals at the cutoff misses that payroll.",
            "Open item: the Retro Change Cutoff that the costing courses use is not on the published calendar. Payroll or Finance to say where it is published.",
            "Open item: the 2027 calendar adds a Semi Monthly payroll that no course covers, and lists no off-cycle runs. Payroll to say who is paid semi-monthly and what changes for HCMs.",
            "Open item: confirm that the HR/Payroll Calendar is what HCMs call the shared administrative calendar, and who maintains it."],
     docs=[("Vanderbilt: Pay Calendar (People Experience)", "https://hr.vanderbilt.edu/compensation/payroll-calendar/"),
           ("Oracle: Overview of Payroll Definitions", "https://docs.oracle.com/en/cloud/saas/human-resources/faucf/overview-of-payroll-definitions.html"),
           ("Oracle: Recalculate Payroll for Retroactive Changes", "https://docs.oracle.com/en/cloud/saas/human-resources/faagp/recalculate-payroll-for-retroactive-changes.html")],
     quiz=[
      dict(q="Where do you find this year's payroll deadlines?", o=["The HR/Payroll Calendar on the People Experience site", "Last month's dates, which repeat every month", "The email your manager sent at the start of the year"], a=0, why="The calendar is published for each year and is the source of truth. Dates move around holidays."),
      dict(q="It is December 2026. When is the monthly HCM Transaction Cutoff?", o=["December 18, as in other months", "December 16, moved for winter break", "December 31, the paycheck date"], a=1, why="The cutoff is the 18th in most months, but December is early. In 2026 it is December 16."),
      dict(q="When are weekly time cards due?", o=["Friday, the day the paycheck goes out", "The 18th, with the monthly cutoff", "Noon on the Monday after the period ends"], a=2, why="The Time Card Due column gives noon on the Monday after the pay period ends. Holiday weeks move it."),
     ],
     pending="Built from Vanderbilt's published HR/Payroll Calendar and Oracle documentation. Not yet reviewed by Payroll; confirm the open items before release."),
    ]

# What to confirm for each new course (shown as the Screen check note on the course page).
VERIFY_A = {
    "shared-calendar": ["that the HR/Payroll Calendar is what HCMs call the shared administrative calendar, and who maintains it", "where the Retro Change Cutoff is published", "who is paid semi-monthly from 2027, and whether off-cycle runs continue"],
    "what-to-attach": ["for each transaction, which documents are required and which are optional", "where each document is filed", "who decides when a course says If finance asks"],
    "who-owns-what": ["approval chains by transaction type", "who enters costing in each area", "the name of the team that processes moves from a requisition"],
    "pay-rules": ["when Vanderbilt's workweek starts and ends", "whether PTO and holiday hours count toward overtime", "holiday pay rules and pay codes", "shift differential rates and pay codes", "on-call and call-back pay rules", "that each DOL link opens"],
    "common-pay-errors": ["the errors payroll corrects most often, with counts", "who to contact for corrections", "how often this list is refreshed"],
}
