# variant_data.py - VARIANT A (last digit 0, 4 or 8): AgroSettle
REG_NO = "B23F0001SE040"      

# (id, release, hours, description)
CHANGES = [
 ("CR01", "R1", 22, "Wrong total when a farmer has two delivery slips on one day (ticket T-114)"),
 ("CR02", "R1", 48, "Cooperative board requests a quality-grade bonus line on advices (REQ-31)"),
 ("CR03", "R1", 30, "Bank changes its payment file format; the export job writes the new layout"),
 ("CR04", "R2", 52, "Field officers request a weekly moisture-discount report (REQ-37)"),
 ("CR05", "R2", 24, "Nightly job abends when a slip has a blank village code (ticket T-131)"),
 ("CR06", "R2", 26, "Mainframe upgrade removes the old sort utility; job steps rewritten for the new one"),
 ("CR07", "R3", 45, "Board requests advance-payment limits per farmer (REQ-52)"),
 ("CR08", "R3", 28, "Payment is 1 rupee short when weight ends in .5 kg (ticket T-160)"),
 ("CR09", "R3", 27, "Analyst, with no ticket or request, splits the 1,900-line rate routine; no behaviour change"),
 ("CR10", "R4", 55, "Board requests multi-crop price bands (REQ-66); the rate routine had to be cleaned up first because it was too tangled to extend"),
 ("CR11", "R4", 30, "Tax regulator requires a reference number on withholding certificates (notice in file REG-2)"),
 ("CR12", "R4", 16, "Wrong crop code printed on the advice for sugarcane (ticket T-188)"),
 ("CR13", "R5", 52, "Board requests SMS payment notices (REQ-74)"),
 ("CR14", "R5", 46, "Bank retires the old file-transfer service; the job moves to the new secure service"),
]

MY_CLASS = dict.fromkeys([c[0] for c in CHANGES], "")   # T1: fill in (see Task T1)

MY_CLASS["CR01"] = "corrective"
MY_CLASS["CR02"] = "perfective"
MY_CLASS["CR03"] = "adaptive"
MY_CLASS["CR04"] = "perfective"
MY_CLASS["CR05"] = "corrective"
MY_CLASS["CR06"] = "adaptive"
MY_CLASS["CR07"] = "perfective"
MY_CLASS["CR08"] = "corrective"
MY_CLASS["CR09"] = "preventive"
MY_CLASS["CR10"] = "perfective"
MY_CLASS["CR11"] = "adaptive"
MY_CLASS["CR12"] = "corrective"
MY_CLASS["CR13"] = "perfective"
MY_CLASS["CR14"] = "adaptive"
 
RELEASES = {  # kloc = thousand lines of code, cc = average cyclomatic complexity per routine
 "R1": dict(kloc=120, cc=11.2, defects=14), 
 "R2": dict(kloc=128, cc=12.0, defects=17),
 "R3": dict(kloc=137, cc=13.1, defects=21), 
 "R4": dict(kloc=147, cc=14.5, defects=26),
 "R5": dict(kloc=158, cc=16.2, defects=33),
}
 
PROFILE = {  # scores 1 (worst) to 5 (best) for every factor
 "name": "AgroSettle", "years_in_production": 31,
 "facts": [
  "F1 About 180,000 lines of COBOL, run as nightly batch jobs on the cooperative's mainframe.",
  "F2 No specification exists; the last COBOL programmer left 4 years ago; comments describe old versions.",
  "F3 It pays 41,000 farmers each season; 9 other systems read its output files.",
  "F4 A one-day stop delays every farmer's payment and breaks the cooperative's licence conditions.",
  "F5 No nightly run has failed in 6 years; operators say they 'never touch the rate routines'.",
  "F6 The last fix to a rate routine needed 3 weeks of testing before anyone trusted it.",
 ],
 "quality": {"complexity": 1, "modularity": 2, "test_coverage": 1,
            "documentation_accuracy": 2, "change_safety": 2},
 "value": {"central_to_daily_operations": 5, "people_who_depend_on_it": 5, "cost_of_absence": 5},
 "rules_still_valid_pct": 90, "alternative_fit_pct": 30,
 "platform_end_of_support_months": None, "key_expert_leaving_months": None,
}