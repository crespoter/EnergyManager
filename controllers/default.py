import datetime
def update():
    #v1.1
    sysTime=str(datetime.datetime.now())
    date=sysTime.split(' ')[0]
    time=sysTime.split(' ')[1].split('.')[0]
    devId=int(request.vars.deviceid);
    device=db().select(db.devices.ALL);
    for x in device:
        if(devId==x.id):
            if(str(request.vars.password)!=str(x.device_password)):
                return "invalid password"
            energyUsed=request.vars.consumed
            db(x.id==db.devices.id).update(energyConsumed=db.devices.energyConsumed+energyUsed,date_of_measure=date,time_of_measure=time)
            db.commit()
            db.consumption.insert(user_id=x.user_id,date_of_measure=date,time_of_measure=time,powerConsumed=energyUsed)
            return "success"
    return "invalid id"
    
def index():
    return dict()
def signup():
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
