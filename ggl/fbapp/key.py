def missing_key(a,user_profile):
       for i in range(len(a)):
        count=0
        if a[i]=='id':
          count=1
          break
       if count!=1:
        updat_dict={'id':0}
        user_profile.update(updat_dict)
       count1=0
       for i in range(len(a)):
        if a[i]=='relationship_status':
         count1=1
         break
       if count1!=1:
        updat_dict={'relationship_status':'nill'}
        user_profile.update(updat_dict)
       count2=0
       for i in range(len(a)):
        if a[i]=='religion':
         count2=1
         break
       if count2!=1:
        updat_dict={'religion':'nill'}
        user_profile.update(updat_dict)
       count3=0
       for i in range(len(a)):
        if a[i]=='birthday':
         count3=1
         break
       if count3!=1:
        updat_dict={'birthday':'nill'}
        user_profile.update(updat_dict)
       count4=0
       for i in range(len(a)):
        if a[i]=='location':
         count4=1
         break
       if count4!=1:
        updat_dict={'location':{'name':'nill'}}
        user_profile.update(updat_dict)
       count5=0
       for i in range(len(a)):
        if a[i]=='hometown':
         count5=1
         break
       if count5!=1:
        updat_dict={'hometown':{'name':'nill'}}
        user_profile.update(updat_dict)
       count6=0
       for i in range(len(a)):
        if a[i]=='email':
         count6=1
         break
       if count6!=1:
        updat_dict={'email':'nill'}
        user_profile.update(updat_dict)
       count7=0
       for i in range(len(a)):
        if a[i]=='education':
         count7=1
         break
       if count7!=1:
        updat_dict={'education':[{'school':{'id':0,'name':'nill'},'type':'nill'}]}
        user_profile.update(updat_dict)
      
