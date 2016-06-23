from django.contrib import admin
import models as md
# Register your models here.
admin.site.register(md.TbCropsinfo)
admin.site.register(md.TbArea)
admin.site.register(md.TbField)
admin.site.register(md.TbPesticidesinfo)
admin.site.register(md.TbFertilizerinfo)
admin.site.register(md.TbPutfertilizer)
admin.site.register(md.TbPutpesticides)
admin.site.register(md.TbRealtimedata)
admin.site.register(md.TbTreatmanage)
admin.site.register(md.TbWarnlimit)