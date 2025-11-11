import sys
if len(sys.argv)==3:
    script_name=sys.argv[0]
    weight=sys.argv[1]
    height=sys.argv[2]  
    print("user provided inputs")
else:
    script_name=sys.argv[0]
    weight="70"
    height="1.75"
    print("default inputs")
bmi=float(weight)/(float(height)*float(height))
print("Script Name:",script_name)
print("Weight (kg):",weight)        
print("Height (m):",height)
print("BMI:",bmi)
