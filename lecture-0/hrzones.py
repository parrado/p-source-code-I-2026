# Ask user for age
age=int(input('Enter your age: '))

# Estimate maximum heart rate based on age
m=208-0.7*age

# Print estimation of maximum heart rate
print(f'Your max heart rate is {m} bpm')

# Ask for number of workouts
n=int(input('Enter number of workouts: '))

# Make room for heart rate values of each workout
#hrs=[0.0]*n
hrs=[]

# For loop
for i in range(n):
    hr=int(input(f'Enter HR for workout {i+1} in bpm: '))        
    #hrs[i]=hr
    hrs.append(hr)

zones=[]
i=0
for hr in hrs:
    if hr<0.5*m:
        zones.append('z0')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1
        break

    if (0.5*m)<=hr<(0.6*m):
        zones.append('z1')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1        
        continue
   
    if (0.6*m)<=hr<(0.7*m):
        zones.append('z2')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1        
        continue
      
    if (0.7*m)<=hr<(0.8*m):
        zones.append('z3')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1        
        continue

    if (0.8*m)<=hr<(0.9*m):        
        zones.append('z4')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1        
        continue

    if (0.9*m)<=hr<=m:
        zones.append('z5')
        print(f'Workout {i+1} was in {zones[i]}')
        i+=1 #i=i+1        
        continue
    





