from django.shortcuts import render,redirect
def home(request):
    result = None
    error_message=""
    
    if request.method == 'POST':
        # Retrieve input values
        num1 = int(request.POST.get('num1', '0'))  
        num2 = int(request.POST.get('num2', '0'))  
        operator = request.POST.get('operator',"")

        if operator == "div" and num2 == 0 :
           error_message = "Error: Division by zero is not allowed."
        else:
           print(error_message)
           if operator =="add":
            result=num1+num2
            print(result)
           elif operator =="sub":
            result=num1 - num2
           elif operator =="mul":
            result=num1 * num2
           elif operator =="div":
            result=num1/num2  
           return render(request, 'index1.html',{'result': result,"error_message": error_message})
        return render(request, 'index.html',{'result': result,"error_message": error_message})
         
    else:
        
        
    
     return render(request, 'index.html')
   

def form(request):
   
    
    return render(request, 'index1.html')

