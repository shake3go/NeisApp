from django.db import models

# Create your models here.

class Teachers(models.Model):
    tId = models.CharField("교사번호",max_length=20, primary_key = True)
    tName = models.CharField("교사이름",max_length=20)
    tPwd = models.CharField("비밀번호", max_length=20)
    authority = models.CharField("권한", max_length=2, default = "00")
    gradeNo = models.CharField("학년", max_length=2, null = True)
    classNo = models.CharField("반", max_length=2, null = True)
    createYMD = models.DateTimeField("데이터생성일자", auto_now_add=True)
    updateYMD = models.DateTimeField("데이터수정일자", auto_now=True, null = True)
    createId = models.CharField("교사번호",max_length=20, null = True)
    updateId = models.CharField("교사번호",max_length=20, null = True)
    objects = models.Manager()

'''
class TeacherPower(models.Model):
    tId = models.ForeignKey(Teacher, on_delete = models.CASCADE)
    authority = models.CharField("권한", max_length=2, default = "00")
    gradeNo = models.CharField("학년", max_length=2, notnull = True, null = True)
    classNo = models.CharField("반", max_length=2, notnull = True, null = True)
    createYMD = models.DateTimeField("데이터생성일자", auto_now_add=True)
    updateYMD = models.DateTimeField("데이터수정일자", auto_now=True, null = True)
    createId = models.CharField("교사번호",max_length=20, primarykey = True)
    updateId = models.CharField("교사번호",max_length=20, primarykey = True)
''' 
class Student(models.Model):
    stdid = models.CharField("학생id", max_length=12, primary_key = True)
    gradeNo = models.CharField("학년", max_length=2)
    classNo = models.CharField("반", max_length=2)
    stdNo = models.CharField("번호", max_length=2)
    stdName = models.CharField("이름", max_length=10)
    stdBirth = models.CharField("생년월일", max_length=6)
    createYMD = models.DateTimeField("데이터생성일자", auto_now_add=True)
    updateYMD = models.DateTimeField("데이터수정일자", auto_now=True, null = True)
    objects = models.Manager()

class Code(models.Model):
    type1 = models.CharField("구분1", max_length=1, primary_key = True)
    type2 = models.CharField("구분2", max_length=2)
    type3 = models.CharField("구분3", max_length=3)
    content = models.TextField("내용")
    createYMD = models.DateTimeField("데이터생성일자", auto_now_add=True)
    createId = models.CharField("교사번호",max_length=20, null = True)
    objects = models.Manager()
    class Meta:
        unique_together = (("type1", "type2", "type3"),)

class StdRecord(models.Model):
    stdid = models.ForeignKey(Student, on_delete = models.CASCADE)
    createYMD = models.DateTimeField("데이터생성일자", auto_now_add=True, primary_key = True)
    tid = models.ForeignKey(Teachers, on_delete = models.CASCADE)
    recodeType = models.ForeignKey(Code, on_delete = models.CASCADE)
    viewLv = models.CharField("보안레벨", max_length=1, default="A")
    content = models.TextField("내용")
    readChk = models.BooleanField("확인", default=False)
    updateYMD = models.DateTimeField("데이터수정일자", auto_now=True)   
    objects = models.Manager() 
    class Meta:
        unique_together = (("stdid", "createYMD", "tid"),)
    
    