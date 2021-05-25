def applicant_selector(gpa, ps_score, ec_count):
      if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3:
        return "This applicant should be accepted."
      elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3:
        return "This applicant should be given an in-person interview."
      else:
        return "This applicant should be rejected."