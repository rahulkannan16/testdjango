from django.shortcuts import render
from django.http import HttpResponse
# from skywalking import agent, config

# config.init(agent_collector_backend_services='10.8.7.222:11800', agent_protocol='grpc',
#             agent_name='django-app',
#             agent_experimental_fork_support=True,
#             agent_logging_level='DEBUG',
#             agent_log_reporter_active=True,
#             agent_meter_reporter_active=True,
#             agent_profile_active=True)


# agent.start()



def demo(request):
    return HttpResponse("Hello, world.")
