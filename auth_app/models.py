# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ArsysAcademicYear(models.Model):
    academic_year = models.CharField(max_length=11, blank=True, null=True)
    letter_date = models.DateTimeField(blank=True, null=True)
    semester = models.CharField(max_length=255, blank=True, null=True)
    numbering = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_academic_year'


class ArsysDefenseApproval(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.BigIntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    approver_id = models.IntegerField(blank=True, null=True)
    approver_role = models.IntegerField(blank=True, null=True)
    decision = models.IntegerField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_approval'


class ArsysDefenseDecision(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=15, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_decision'


class ArsysDefenseExaminer(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    examiner_id = models.IntegerField(blank=True, null=True)
    applicant_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    additional = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_examiner'


class ArsysDefenseExaminerDecisionLog(models.Model):
    defense_examiner_id = models.IntegerField(blank=True, null=True)
    defense_decision_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_examiner_decision_log'


class ArsysDefenseExaminerPresence(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    defense_examiner_id = models.IntegerField(blank=True, null=True)
    examiner_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    decision_id = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_examiner_presence'


class ArsysDefenseExaminerRubric(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    defense_examiner_id = models.IntegerField(blank=True, null=True)
    defense_rubric_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_examiner_rubric'


class ArsysDefenseModel(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_model'


class ArsysDefenseRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_role'


class ArsysDefenseRubric(models.Model):
    rubric_id = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    role = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_rubric'


class ArsysDefenseRubricBase(models.Model):
    program_id = models.IntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    item = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_rubric_base'


class ArsysDefenseScoreGuide(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    sequence = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_defense_score_guide'


class ArsysDefenseSupervisorPresence(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    research_supervisor_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    research_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_defense_supervisor_presence'


class ArsysDiscussion(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    discussion_type = models.IntegerField(blank=True, null=True)
    discussant_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_discussion'


class ArsysDiscussionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    description = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_discussion_type'


class ArsysEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    event_type_id = models.IntegerField(blank=True, null=True)
    application_deadline = models.DateTimeField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    draft_deadline = models.DateTimeField(blank=True, null=True)
    quota = models.IntegerField(blank=True, null=True)
    current = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    completed = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_event'


class ArsysEventApplicantDefense(models.Model):
    id = models.BigAutoField(primary_key=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    research_id = models.BigIntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)
    space_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    publish = models.IntegerField(blank=True, null=True)
    report = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_applicant_defense'


class ArsysEventApplicantSeminar(models.Model):
    id = models.BigAutoField(primary_key=True)
    room_id = models.IntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    research_id = models.BigIntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    confirmed = models.IntegerField(blank=True, null=True)
    publish = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_applicant_seminar'


class ArsysEventApplicantSeminarExtra(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_applicant_seminar_extra'


class ArsysEventLetter(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_letter'


class ArsysEventLetterType(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    ina_description = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_event_letter_type'


class ArsysEventSession(models.Model):
    time = models.CharField(max_length=11, blank=True, null=True)
    examination_type = models.CharField(max_length=15, blank=True, null=True)
    day = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_session'


class ArsysEventSpace(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_event_space'


class ArsysEventType(models.Model):
    code = models.CharField(max_length=3, blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    examination_type = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    ina_description = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_event_type'


class ArsysInstitutionCluster(models.Model):
    program_id = models.IntegerField(blank=True, null=True)
    cluster_base_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_cluster'


class ArsysInstitutionClusterBase(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_cluster_base'


class ArsysInstitutionConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    config_base_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_config'


class ArsysInstitutionConfigBase(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_config_base'


class ArsysInstitutionDepartment(models.Model):
    faculty_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_department'


class ArsysInstitutionFaculty(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    university_id = models.IntegerField(blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    name_eng = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_faculty'


class ArsysInstitutionFacultyLetter(models.Model):
    id = models.BigAutoField(primary_key=True)
    faculty_id = models.IntegerField(blank=True, null=True)
    faculty_letter_base_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_faculty_letter'


class ArsysInstitutionFacultyLetterBase(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    ina_description = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_institution_faculty_letter_base'


class ArsysInstitutionProgram(models.Model):
    faculty_id = models.IntegerField(blank=True, null=True)
    level_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    abbrev = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_eng = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_id = models.CharField(max_length=255, blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    letter_code = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_program'


class ArsysInstitutionProgramLetter(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    program_letter_base_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_program_letter'


class ArsysInstitutionProgramLetterBase(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    ina_description = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_institution_program_letter_base'


class ArsysInstitutionProgramLevel(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    name_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_program_level'


class ArsysInstitutionRole(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_institution_role'


class ArsysInstitutionSpecialization(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_specialization'


class ArsysInstitutionStudyCompletion(models.Model):
    program_id = models.IntegerField(blank=True, null=True)
    study_completion_base_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_study_completion'


class ArsysInstitutionStudyCompletionBase(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_study_completion_base'


class ArsysInstitutionStudyCompletionTeam(models.Model):
    study_completion_id = models.IntegerField(blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_study_completion_team'


class ArsysInstitutionUniversity(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_institution_university'


class ArsysResearch(models.Model):
    id = models.BigAutoField(primary_key=True)
    milestone_id = models.IntegerField(blank=True, null=True)
    academic_year_id = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)
    student_id = models.BigIntegerField(blank=True, null=True)
    code = models.CharField(max_length=15, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_research'


class ArsysResearchConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    config_base_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_config'


class ArsysResearchConfigBase(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_config_base'


class ArsysResearchDecisionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    description = models.CharField(max_length=15, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_decision_type'


class ArsysResearchDefenseType(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    research_type_base_id = models.IntegerField(blank=True, null=True)
    supervisor_number = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    week_of_supervise = models.IntegerField(blank=True, null=True)
    enable_week_of_supervise = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_defense_type'


class ArsysResearchFile(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    file_type = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_file'


class ArsysResearchFileSupervisor(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    file_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_file_supervisor'


class ArsysResearchFileType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=12, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_file_type'


class ArsysResearchInformation(models.Model):
    code = models.CharField(max_length=7, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_information'


class ArsysResearchLetter(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    research_letter_base_id = models.IntegerField(blank=True, null=True)
    faculty_letter_id = models.IntegerField(blank=True, null=True)
    faculty_letter_number = models.IntegerField(blank=True, null=True)
    faculty_letter_date = models.DateTimeField(blank=True, null=True)
    faculty_letter_date_back = models.CharField(max_length=50, blank=True, null=True)
    program_letter_id = models.IntegerField(blank=True, null=True)
    program_letter_number = models.IntegerField(blank=True, null=True)
    program_letter_date = models.DateTimeField(blank=True, null=True)
    program_letter_date_back = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expire_date_back = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_letter'


class ArsysResearchLetterBase(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=40, blank=True, null=True)
    ina_description = models.CharField(max_length=40, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_research_letter_base'


class ArsysResearchLog(models.Model):
    type_id = models.IntegerField(blank=True, null=True)
    research_id = models.IntegerField(blank=True, null=True)
    loger_id = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_log'


class ArsysResearchLogType(models.Model):
    code = models.CharField(max_length=15, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_a = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_log_type'


class ArsysResearchMilestone(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    research_model_id = models.IntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    phase = models.CharField(max_length=50, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_milestone'


class ArsysResearchMilestoneLog(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    research_model_id = models.IntegerField(blank=True, null=True)
    milestone_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_milestone_log'


class ArsysResearchMilestoneModel(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_milestone_model'


class ArsysResearchMilestoneSeminar(models.Model):
    id = models.BigAutoField(primary_key=True)
    milestone = models.CharField(max_length=20, blank=True, null=True)
    milestone_model = models.CharField(max_length=20, blank=True, null=True)
    propose_button = models.IntegerField(blank=True, null=True)
    phase = models.CharField(max_length=50, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_pi = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_milestone_seminar'


class ArsysResearchMilestoneb(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    research_model_id = models.IntegerField(blank=True, null=True)
    phase = models.CharField(max_length=50, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_milestoneb'


class ArsysResearchModel(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_model'


class ArsysResearchRemark(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    discussant_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_remark'


class ArsysResearchReview(models.Model):
    research_id = models.BigIntegerField(blank=True, null=True)
    reviewer_id = models.IntegerField(blank=True, null=True)
    decision_id = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_review'


class ArsysResearchReviewDecisionType(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    description = models.CharField(max_length=15, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_review_decision_type'


class ArsysResearchReviewDiscussion(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    discussant_id = models.IntegerField(blank=True, null=True)
    discussant_type = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_review_discussion'


class ArsysResearchReviewDiscussionRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    reader_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_review_discussion_read'


class ArsysResearchSupervise(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    threader_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    read = models.IntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    date_of_meeting = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervise'


class ArsysResearchSuperviseDiscussion(models.Model):
    id = models.BigAutoField(primary_key=True)
    supervise_id = models.IntegerField(blank=True, null=True)
    discussant_id = models.IntegerField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    read = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervise_discussion'


class ArsysResearchSuperviseDurationDisable(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervise_duration_disable'


class ArsysResearchSupervisor(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    bypass = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor'


class ArsysResearchSupervisorDummy(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor_dummy'


class ArsysResearchSupervisorExternal(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    supervisor_name = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor_external'


class ArsysResearchSupervisorExternalDummy(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    supervisor_name = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor_external_dummy'


class ArsysResearchSupervisorExtra(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor_extra'


class ArsysResearchSupervisorScore(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    applicant_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    defense_note = models.TextField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_supervisor_score'


class ArsysResearchTurnitin(models.Model):
    research_id = models.IntegerField(blank=True, null=True)
    event_type = models.IntegerField(blank=True, null=True)
    approval = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_turnitin'


class ArsysResearchType(models.Model):
    id = models.BigAutoField(primary_key=True)
    program_id = models.IntegerField(blank=True, null=True)
    research_type_base_id = models.IntegerField(blank=True, null=True)
    alternative_name = models.CharField(max_length=255, blank=True, null=True)
    supervisor_number = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    week_of_supervise = models.IntegerField(blank=True, null=True)
    enable_week_of_supervise = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_type'


class ArsysResearchTypeBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    research_model_id = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    level_id = models.CharField(max_length=20, blank=True, null=True)
    supervisor_number = models.IntegerField(blank=True, null=True)
    week_of_supervise = models.IntegerField(blank=True, null=True)
    enable_week_of_supervise = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_type_base'


class ArsysResearchTypeExamination(models.Model):
    id = models.BigAutoField(primary_key=True)
    research_type_id = models.IntegerField(blank=True, null=True)
    defense_model_id = models.IntegerField(blank=True, null=True)
    event_type_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_research_type_examination'


class ArsysSeminarExaminer(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    examiner_id = models.IntegerField(blank=True, null=True)
    additional = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_seminar_examiner'


class ArsysSeminarExaminerPresence(models.Model):
    defense_model_id = models.IntegerField(blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    applicant_id = models.IntegerField(blank=True, null=True)
    seminar_examiner_id = models.IntegerField(blank=True, null=True)
    examiner_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    decision = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_seminar_examiner_presence'


class ArsysSeminarRoom(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    room_code = models.CharField(max_length=10, blank=True, null=True)
    space_id = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField(blank=True, null=True)
    moderator_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_seminar_room'


class ArsysSeminarSupervisorPresence(models.Model):
    defense_model_id = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    research_supervisor_id = models.IntegerField(blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    research_id = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_seminar_supervisor_presence'


class ArsysStaff(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    sso = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    univ_code = models.CharField(max_length=4, blank=True, null=True)
    employee_id = models.CharField(max_length=20, blank=True, null=True)
    old_employee_id = models.CharField(max_length=20, blank=True, null=True)
    front_title = models.CharField(max_length=15, blank=True, null=True)
    rear_title = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    staff_type_id = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    structure_id = models.IntegerField(blank=True, null=True)
    specialization_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_staff'


class ArsysStaffPosition(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_staff_position'


class ArsysStaffRole(models.Model):
    staff_id = models.IntegerField(blank=True, null=True)
    staff_role_base_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_staff_role'


class ArsysStaffRoleBase(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    user_role = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_staff_role_base'


class ArsysStaffStatus(models.Model):
    code = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    description_eng = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_staff_status'


class ArsysStaffStructure(models.Model):
    position_id = models.IntegerField(blank=True, null=True)
    structure = models.CharField(max_length=20, blank=True, null=True)
    classification = models.CharField(max_length=5, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_staff_structure'


class ArsysStaffType(models.Model):
    code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_staff_type'


class ArsysStudent(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    program_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    specialization_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    supervisor_id = models.IntegerField(blank=True, null=True)
    gpa = models.CharField(db_column='GPA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'arsys_student'


class ArsysTelegram(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arsys_telegram'


class Cache(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheLocks(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    owner = models.CharField(max_length=255)
    expiration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cache_locks'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    field = models.CharField(max_length=255)
    upload = models.ForeignKey('Uploads', models.DO_NOTHING)
    model_type = models.CharField(max_length=255)
    model_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class JobBatches(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    total_jobs = models.IntegerField()
    pending_jobs = models.IntegerField()
    failed_jobs = models.IntegerField()
    failed_job_ids = models.TextField()
    options = models.TextField(blank=True, null=True)
    cancelled_at = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField()
    finished_at = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_batches'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class Messages(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile_country_code = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    has_read = models.IntegerField()
    sender_type = models.CharField(max_length=255, blank=True, null=True)
    sender_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.CharField(max_length=36)
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    user_id = models.PositiveBigIntegerField()
    client_id = models.CharField(max_length=36)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    owner_type = models.CharField(max_length=255, blank=True, null=True)
    owner_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=255, blank=True, null=True)
    redirect_uris = models.TextField()
    grant_types = models.TextField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthDeviceCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.CharField(max_length=36)
    user_code = models.CharField(unique=True, max_length=8)
    scopes = models.TextField()
    revoked = models.IntegerField()
    user_approved_at = models.DateTimeField(blank=True, null=True)
    last_polled_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_device_codes'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    access_token_id = models.CharField(max_length=80)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class PasswordResetTokens(models.Model):
    email = models.CharField(primary_key=True, max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_reset_tokens'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PermissionRole(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)  # The composite primary key (permission_id, role_id) found, that is not supported. The first column is selected.
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permission_role'
        unique_together = (('permission', 'role'),)


class PermissionUser(models.Model):
    permission = models.ForeignKey('Permissions', models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=255)
    team = models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission_user'
        unique_together = (('user_id', 'permission', 'user_type', 'team'),)


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class RoleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField()
    user_type = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_user'
        unique_together = (('user_id', 'role', 'user_type', 'team'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    display = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class UploadPermits(models.Model):
    id = models.BigAutoField(primary_key=True)
    upload = models.ForeignKey('Uploads', models.DO_NOTHING)
    user_id = models.PositiveBigIntegerField()
    permitter_id = models.PositiveBigIntegerField(blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'upload_permits'


class Uploads(models.Model):
    id = models.BigAutoField(primary_key=True)
    hash = models.CharField(max_length=350)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    size = models.BigIntegerField()
    extension = models.CharField(max_length=20)
    mime = models.CharField(max_length=50)
    disk = models.CharField(max_length=255, blank=True, null=True)
    visitable = models.IntegerField()
    visits = models.PositiveBigIntegerField()
    private = models.IntegerField()
    thumbnail_id = models.PositiveBigIntegerField(blank=True, null=True)
    uploader_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    sso = models.CharField(max_length=20, blank=True, null=True)
    telegram_chat_id = models.CharField(max_length=15, blank=True, null=True)
    telegram_blocked = models.IntegerField(blank=True, null=True)
    telegram_bypass = models.IntegerField(blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    google_id = models.CharField(max_length=50, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
