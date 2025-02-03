class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Requested Path: {request.path}") 
        if request.path == "/":  
            print("Custom Middleware: Login View Accessed")

        response = self.get_response(request)
        return response


#function based

# def custom_middleware(get_response):
#     def middleware(request):
#         if request.path == "/":  # Check if it's the login view
#             print("Function-Based Middleware: Login View Accessed")
        
#         response = get_response(request)
#         return response

#     return middleware
