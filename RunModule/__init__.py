from shared import enums, helpers

import azure.functions as func
import importlib
import logging


async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        bot_module_name = req.route_params.get('moduleName')
        command_name = req.route_params.get('commandName')
        args = req.params.copy()

        logging.info(bot_module_name)
        logging.info(command_name)
        logging.info(args)

        module_type = importlib.import_module(f'modules.{bot_module_name.lower()}')
        bot_module = helpers.igetattr(module_type, bot_module_name)()
        result = helpers.igetattr(bot_module, command_name)(**args)

        return func.HttpResponse(
            #"This HTTP triggered function executed successfully.",
            str(result),
            status_code=enums.HttpStatusCode.OK.value
        )
    except ValueError as error:
        # not gonna bother logging here, as these are for known errors caused by e.g. bad user input
        return func.HttpResponse(
            #"This HTTP triggered function executed successfully.",
            error.args[0],
            status_code=enums.HttpStatusCode.INTERNAL_SERVER_ERROR.value
        )
    except Exception:
        # any expected errors get logged here
        message = 'unexpected error occurred'
        logging.exception(message)

        return func.HttpResponse(
            #"This HTTP triggered function executed successfully.",
            message,
            status_code=enums.HttpStatusCode.INTERNAL_SERVER_ERROR.value
        )
