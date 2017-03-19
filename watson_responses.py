from watson_developer_cloud import ConversationV1
import json
import config

class watson:
    def __init__(self):
        self.workspace_id = config.workspace_id
        self.conversation = ConversationV1(
            username= config.watson_username,
            password= config.watson_password,
            version='2017-02-03')
        self.our_context = dict()
    def get_response(self,bot_response):
        response = self.conversation.message(workspace_id=self.workspace_id, message_input={
        'text': bot_response},
        context = self.our_context)
        json_string = json.dumps(response, indent=2)
        #print(json_string)

        #global our_context
        self.our_context = response["context"]
        parsed_json = json.loads(json_string)
        if len(parsed_json["output"]["text"])!= 0:
            return parsed_json["output"]["text"][0]
        return ""
        #print self.our_context
