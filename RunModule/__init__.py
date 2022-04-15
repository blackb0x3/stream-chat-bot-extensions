import importlib
from shared.enums import HttpStatusCode

import azure.functions as func
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        bot_module_name = req.route_params.get('moduleName')
        command_name = req.route_params.get('commandName')
        args = req.params.copy()

        logging.info(bot_module_name)
        logging.info(command_name)
        logging.info(args)

        module_type = importlib.import_module(f'modules.{bot_module_name.lower()}')
        bot_module = getattr(module_type, bot_module_name)()
        result = getattr(bot_module, command_name)(**args)

        return func.HttpResponse(
            #"This HTTP triggered function executed successfully.",
            str(result),
            status_code=HttpStatusCode.OK.value
        )
    except Exception:
        # any expected errors get logged here
        message = 'unexpected error occurred'
        logging.exception(message)

        return func.HttpResponse(
            #"This HTTP triggered function executed successfully.",
            message,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value
        )
