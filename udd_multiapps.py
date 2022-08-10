#!/u01/app/oracle/apr2022/wls12c/oracle_common/common/bin/wlst.sh
def wlDeployUndeploy(username, password, adminURL, appName, location, targets):
    try:
        #connect to admin server
        connect(username, password, adminURL)
        #start edit operation
        edit()
        startEdit()

        #stop application
        stopApplication(appName)

        #start undeploying application to "AdminServer" server
        progress = undeploy(appName, timeout=60000)
        progress.printStatus()
        save()
        activate(20000,block="true")
        #start deploying application to ""AdminServer" server
        progress = deploy(appName,location,targets)
        progress.printStatus()
        #print 'Done deploying application' +appname

    except Exception, e:
         print ex.toString()
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.158.114:7001','benefits','test/benefits.war','AdminServer')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.158.114:7001','messaging','test/messaging.war','AdminServer')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.158.114:7001','contacts','test/contacts.war','AdminServer')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.158.114:7001','supplies','test/supplies.war','AdminServer')

