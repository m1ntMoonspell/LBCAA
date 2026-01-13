from maa.agent.agent_server import AgentServer
from maa.custom_action import CustomAction
from maa.context import Context
    
@AgentServer.custom_action("MultiClick")
class MultiClick(CustomAction):

    def run(
        self,
        context:Context,
        argv:CustomAction.RunArg,
    ) -> CustomAction.RunResult:
        print(123)
        return CustomAction.RunResult(success=True)