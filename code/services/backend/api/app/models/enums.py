from enum import Enum

# Enum dla working_time w tabeli Jobs
class WorkingTimeEnum(str, Enum):
    full_time = 'full-time'
    part_time = 'part-time'
    temporary = 'temporary'

# Enum dla contract_type w tabeli Jobs
class ContractTypeEnum(str, Enum):
    employment = 'employment'
    contract = 'contract'
    task_specific = 'task-specific'
    internship = 'internship'
    b2b = 'b2b'

# Enum dla work_type w tabeli Jobs
class WorkTypeEnum(str, Enum):
    stationary = 'stationary'
    hybrid = 'hybrid'
    remote = 'remote'
    mobile = 'mobile'

# Enum dla level w tabeli ReportEducations
class EducationLevelEnum(str, Enum):
    primary = 'primary'
    secondary = 'secondary'
    bachelor = 'bachelor'
    master = 'master'
    doctorate = 'doctorate'
    vocational = 'vocational'
    continuing = 'continuing'

# Enum dla level w tabeli ReportLanguages
class LangEnum:
    A1 = 'beginner'
    A2 = 'elementary'
    B1 = 'intermediate'
    B2 = 'upper-intermediate'
    C1 = 'advanced'
    C2 = 'proficient'
