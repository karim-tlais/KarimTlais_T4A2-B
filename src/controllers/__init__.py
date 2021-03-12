from controllers.profile_controller import profile , index , process
from controllers.vaccine_controller import vaccine , vaccination , vprocess
from controllers.auth_controller import login , signup , logout

registerable_controllers = [
    profile,
    index,
    process,
    vaccine,
    vaccination,
    vprocess,
    login,
    signup,
    logout
]