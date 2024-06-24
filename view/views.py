from fastapi import status,HTTPException,APIRouter,Request
from helper_functions import get_current_date,validate_output_list,setup_logger
from model.api_request import ApiRequestModel
from model.api_response import ApiResponseModel
from controller.process_controller import execute_adddition_procedure

logger = setup_logger()
router = APIRouter()


@router.post('/add_list',status_code=200,response_model=ApiResponseModel)
def additionIntegerslist(model: ApiRequestModel):
	batchid=model.batchid
	input_data=model.payload
	logger.info('-----Batch id ------ {batchid} and {input_data}')
	start_date=get_current_date()
	output=execute_adddition_procedure(input_data)
	if input_data is None:
		logger.error('Input data is not available')
		raise HTTPException(status_code=409,detail='not found')
	elif validate_output_list(output):
		logger.error('Output data is blank')
		raise HTTPException(status_code=418,detail='Empty output')
	else:
		logger.info("Processing is complete with "+str(output))
		ApiResponseModel.batchid=batchid
		ApiResponseModel.response=output
		ApiResponseModel.status="complete"
		ApiResponseModel.started_at=start_date
		ApiResponseModel.completed_at=get_current_date()
		return ApiResponseModel
            
