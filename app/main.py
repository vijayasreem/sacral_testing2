@app.post("/validate_policy/")
def validate_policy():
  data = request.json
  sum_assured = data["sum_assured"]
  age = data["age"]
  annual_income = data["annual_income"]
  spouse = data["spouse"]
  otp_status = data["otp_status"]
  
  #Validate min and max sum assured
  if sum_assured < 50K or sum_assured > 2lac:
    return {"message": "Sum assured is not valid"}
  
  #Validate min and max age limits
  if age < 18 or age > 70:
    return {"message": "Age is not valid"}
  
  #Validate annual income
  if annual_income < 40000:
    return {"message": "Annual income is not valid"}
  
  #Validate OTP authentication
  if otp_status == False:
    return {"message": "OTP authentication is not valid"}
  
  #Validate spouse eligibility
  if spouse == True and annual_income < 40000:
    return {"message": "Spouse is not eligible for insurance coverage"}
  
  #If all validations are successful
  return {"message": "Policy issued successfully"}