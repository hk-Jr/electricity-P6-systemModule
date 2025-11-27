
import sys
if len(sys.argv) != 2:
    units = float(sys.argv[1])

else:
  units=100
rate_per_unit = 5
bill_amount = units * rate_per_unit

print(f"Units Consumed: {units}")
print(f"Rate per Unit: ₹{rate_per_unit}")
print(f"Total Electricity Bill: ₹{bill_amount}")
