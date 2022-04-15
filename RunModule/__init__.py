import azure.functions as func
import logging

from shared.enums import HttpStatusCode

ARG_DELIMITER = '|'


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    module_name = req.route_params.get('moduleName')
    command_name = req.route_params.get('commandName')
    args = req.route_params.get('args').split(ARG_DELIMITER)

    logging.debug({ module_name, command_name, args })

    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=HttpStatusCode.OK.value
    )
