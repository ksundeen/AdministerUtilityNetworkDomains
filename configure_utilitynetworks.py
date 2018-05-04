import arcpy

# Build UN

instance_name = 'MNWEBGIS-PRI'

domainNetwork = {
    'gas': {
        'gdbName': '',
        'sdeConnection': 
        'datasetName': '',
        'assetPackagePath': '',
        'utilityNetworkName': '',
        'domain_networks': ['Structure', 'Gas']

    },
    'water': {}
    'electric': {}
}

for domain in domainNetwork:

    # Create Postgresql Enterprise GDB
    arcpy.CreateEnterpriseGeodatabase_management (
        database_platform='PostgreSQL', 
        instance_name=instance_name, 
        database_name=domain['gdbName'], 
        account_authentication='DATABASE_AUTH', 
        database_admin='postgres', 
        database_admin_password='postgres', 
        sde_schema='SDE_SCHEMA', 
        gdb_admin_name='sde', 
        gdb_admin_password='gisisfunandcool1!', 
        tablespace_name='#', 
        authorization_file='C:/Program Files/ESRI/License10.6/sysgen/keycodes')

    # Create SDE Connection Files (for sde user)
    arcpy.CreateDatabaseConnection_management (
        out_folder_path=, 
        out_name=, 
        database_platform='POSTGRESQL', 
        instance=instance_name, 
        account_authentication='DATABASE_AUTH', 
        username='sde', 
        password='gisisfunandcool1!, 
        save_user_pass='SAVE_USERNAME', 
        database=domain['gdbName'], 
        schema='SDE', 
        version_type='#', 
        version='#', 
        date='#')  

    # Create UNOWNER User
    # arcpy.CreateDatabaseUser_management("C:/gdbconnections/connection_ssi.sde", "OPERATING_SYSTEM_USER", "mynet\\vorhoos")
    arcpy.CreateDatabaseUser_management (
        input_database=domain[, 
        user_authentication_type='DATABASE_USER', 
        user_name='UNOWNER', 
        user_password='UNOWNER',
        role='#', 
        tablespace_name='#')
    
    print('Completed adding db user for ' + domain)
    arcpy.AddMessage('\n...')

    # Create SDE Connection File to UNOWNER
    arcpy.CreateDatabaseConnection_management (
        out_folder_path=, 
        out_name=, 
        database_platform='POSTGRESQL', 
        instance=instance_name, 
        account_authentication='DATABASE_AUTH', 
        username='UNOWNER', 
        password='UNOWNER, 
        save_user_pass='SAVE_USERNAME', 
        database=domain['gdbName'], 
        schema='UNOWNER', 
        version_type='#', 
        version='#', 
        date='#')    

    # Stage Utility Network
    arcpy.StageUtilityNetwork_pt_NOALIAS (
        enterprise_gdb=domain['gdbName'], 
        service_territory_feature_class=, 
        dataset_name=domain['datasetName'], 
        in_utility_network_name=)

    # Apply Asset Package

    # asset_package = 'C:/data/Water_AssetPackage.gdb'
    # utility_network = 'C:/data/connection.sde/gis.SYSTEM/gis.WaterNetwork'
    # domain_networks = ['Structure', 'Water']
    # load = False
    # analyze = False

    arcpy.pt.AssetPackageToUtilityNetwork_pt_NOALIAS (
        asset_package=domain['assetPackagePath'], 
        domain_networks=domain['domain_networks'], 
        in_utility_network=, 
        load_data=True, 
        analyze=True)

    # Export Asset Package (as backup)
    # utility_network = "C:/data/connection.sde/gis.SYSTEM/gis.WaterNetwork"
    # domain_networks = ["Water"]
    # folder = "C:/data"
    # package_name = "Water_export"
    # export_data = False
    arcpy.pt.UtilityNetworkToAssetPackage_pt_NOALIAS (
        in_utility_network=, 
        domain_networks=domain['domain_networks'][1], 
        output_folder=domain + '_export', 
        output_name=, 
        include_data=)

    # Enable Branch Versioning