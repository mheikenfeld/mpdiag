from collections import defaultdict
import logging

def split_sign_variable_wrf(filename,variable,name_neg=None,name_pos=None,add_coordinates=None,constraint=None,absolute_value=False):
    from wrfcube import loadwrfcube
    if name_neg is None:
        name_neg=variable+'_neg'
    if name_pos is None:
        name_pos=variable+'_pos'
    cube=loadwrfcube(filename,variable,add_coordinates=add_coordinates,constraint=constraint)
    list_out=[]
    list_out.append(get_variable_neg(cube,name_neg,absolute_value=absolute_value))
    list_out.append(get_variable_pos(cube,name_pos,absolute_value=absolute_value))
    return list_out

def split_sign_variable_rams(filename,variable,name_neg,name_pos,add_coordinates=None,constraint=None,absolute_value=False):
    from ramscube import loadramscube
    cube=loadramscube(filename,variable,add_coordinates=add_coordinates,constraint=constraint)
    list_out=[]
    list_out.append(get_variable_neg(cube,name_neg,absolute_value=absolute_value))
    list_out.append(get_variable_pos(cube,name_pos,absolute_value=absolute_value))
    return list_out

def get_variable_neg(cube,name_neg,absolute_value=False):
    from copy import deepcopy
    from dask.array import clip
    from numpy import inf
    cube_neg=deepcopy(cube)
    cube_neg.data=clip(cube_neg.core_data(),-inf,0)
    if absolute_value:
        cube_neg.data=abs(cube_neg.core_data())
    cube_neg.rename(name_neg)
    return cube_neg

def get_variable_pos(cube,name_pos,absolute_value=False):
    from copy import deepcopy
    from dask.array import clip
    from numpy import inf
    cube_pos=deepcopy(cube)
    cube_pos.data=clip(cube_pos.core_data(),0,inf)
    if absolute_value:
        cube_pos.data=abs(cube_pos.core_data())
    cube_pos.rename(name_pos)
    return cube_pos
   
List_Processes_Thompson_Mass=[
         'PRW_VCD',   #  Vapor->Water
         'PRV_REV',   #  Vapor->Water
         'PRR_WAU',   #  Vapor->Water
         'PRR_RCW',   #  Vapor->Water
         'PRR_RCS',   #  Vapor->W ater
         'PRR_RCG',   #  Rain-> Graupel
         'PRR_GML',   #  Vapor-> Water
         'PRR_SML',   #  Snow-> Rain
         'PRR_RCI',   #  Vapor->Water
         'PRI_INU',   #  Vapor->Water
         'PRI_IHM',   #  Vapor->Water
         'PRI_WFZ',   #  Vapor->Water
         'PRI_RFZ',   #  Vapor->Water
         'PRI_IDE',   #  Vapor->Water
         'PRI_RCI',   #  Vapor->Water
         'PRI_IHA',   #  Vapor->Water
         'PRS_IAU',   #  Vapor->Water
         'PRS_SCI',   #  Vapor->Water
         'PRS_RCS',   #  Vapor->Water
         'PRS_SCW',   #  Vapor->Water
         'PRS_SDE',   #  Vapor->Water
         'PRS_IHM',   #  Vapor->Water
         'PRS_IDE',   #  Vapor->Water
         'PRG_SCW',   #  Vapor->Water
         'PRG_RFZ',   #  Vapor->Water
         'PRG_GDE',   #  Vapor->Water
         'PRG_GCW',   #  Vapor->Water
         'PRG_RCI',   #  Vapor->Water
         'PRG_RCS',   #  Vapor->Water
         'PRG_RCG',   #  Rain->Graupel
         'PRG_IHM',   #  Graupel->Ice
         'PRW_IMI',   #  Ice -> Water
         'PRI_WFI'    #  Water -> Ice
          ]
          
thompson_processes_mass_split=defaultdict(dict)
thompson_processes_mass_split['PRW_VCD']=['PRW_VCD','E_PRW_VCD']
thompson_processes_mass_split['PRR_RCG']=['PRR_RCG','E_PRR_RCG']
thompson_processes_mass_split['PRG_RCG']=['PRG_RCG','E_PRG_RCG']
thompson_processes_mass_split['PRR_RCS']=['PRR_RCS','E_PRR_RCS']
thompson_processes_mass_split['PRS_RCS']=['PRS_RCS','E_PRS_RCS']
thompson_processes_mass_split['PRI_IDE']=['PRI_IDE','E_PRI_IDE']
thompson_processes_mass_split['PRS_SDE']=['PRS_SDE','E_PRS_SDE']
thompson_processes_mass_split['PRG_GDE']=['PRG_GDE','E_PRG_GDE']


List_Processes_Thompson_Mass_signed=list(List_Processes_Thompson_Mass).extend(['E_PRW_VCD','E_PRR_RCS','E_PRR_RCG','E_PRI_IDE','E_PRS_RCS','E_PRS_SDE','E_PRG_GDE','E_PRG_RCG'])

List_Processes_Thompson_Number=[
         'PNC_WCD',
         'PNC_WAU',
         'PNC_RCW',
         'PNC_SCW',
         'PNC_GCW',
         'PNR_WAU',
         'PNR_RCS',
         'PNR_RCG',
         'PNR_RCI',
         'PNR_SML',
         'PNR_GML',
         'PNR_REV',
         'PNR_RCR',
         'PNR_RFZ',
         'PNI_INU',
         'PNI_IHM',
         'PNI_WFZ',
         'PNI_RFZ',
         'PNI_IDE',
         'PNI_RCI',
         'PNI_SCI',
         'PNI_IAU',
         'PNI_IHA',
         'PNA_RCA',
         'PNA_SCA',
         'PNA_GCA',
         'PNA_RCA',
         'PNA_SCA',
         'PNA_GCA',
         'PND_RCD',
         'PND_SCD',
         'PND_GCD',
         'PNW_IMI',   #  Ice -> Water
         'PNI_WFI'    #  Water -> Ice
                             ]

#Morrison microphysics
morrison_processes_mass=[
    'PRD',
    'EPRD',
    'PRDG',
    'EPRDG',
    'PRDS',
    'EPRDS',
    'PRE',
    'PRA',
    'PRC',
    'PCC',
    'PCCN',
    'PSMLT',
    'EVPMS',
    'QMULTS',
    'QMULTR',
    'PRACS',
    'PSACWG',
    'PGSACW',
    'PGRACS',
    'EVPMG',
    'PGMLT',
    'PRACI',
    'PIACRS',
    'PRACIS',
    'PRACG',
    'QMULTG',
    'MNUCCR',
    'MNUCCC',
    'MNUCCD',
    'QMULTRG',
    'PRAI',
    'PRCI',
    'PSACWS',
    'PIACR',
    'PSACWI',
    'PSACR',
    'QICF', #instantaneous processes (addes by BAW)             
    'QGRF',      
    'QNIRF',
    'QIIM'
    ]
    
Proclist_Morr_mass=list(morrison_processes_mass)

morrison_processes_mass_split=defaultdict(dict)
morrison_processes_mass_split['PCC']=['PCC','EPCC']

Proclist_Morr_mass_signed=list(Proclist_Morr_mass).extend(['EPCC'])

morrison_processes_number=[
    'NSUBC',
    'NSUBI',
    'NSUBS',
    'NSUBR',
    'NNUCCC',
    'NNUCCD',
    'NNUCCR',
    'NPRA',
    'NRAGG',
    'NSAGG',
    'NPRC',
    'NPRC1',
    'NPSACWS',
    'NPSACWI',
    'NPRCI',
    'NPRAI',
    'NMULTS',
    'NMULTR',
    'NPRACS',
    'NSMLTR',
    'NSMLTS',
    'NIACR',
    'NPRACG',
    'NPSACWG',
    'NSCNG',
    'NGRACS',
    'NGMLTG',
    'NGMLTR',
    'NSUBG',
    'NMULTG',
    'NMULTRG,',
    'NIACRS', 
    'NICF', #instantaneous processes (addes by BAW)          
    'NGRF',      
    'NSRF',
    'NIIM'
]


#Start setting things up for the SBM:
    
# SBM Full (Dummy variables at the moment)

#SBMfull_processes_mass=['P_FRZ_ICE',
#                        'P_FRZ_HAIL', 
#                        'P_MLT_ICE',
#                        'P_MLT_SNOW',
#                        'P_MLT_GRAUP',
#                        'P_MLT_HAIL']
SBMfull_processes_mass=['QVAPOR','QCLOUD']
SBMfull_processes_number=['QVAPOR','QCLOUD']
SBMfull_processes_mass_split=dict()
SBMfull_processes_number_split=dict()

List_Processes_RAMS_Mass=[
         'VAPCLDT',
         'VAPRAINT',
         'VAPPRIST',
         'VAPSNOWT',
         'VAPAGGRT',
         'VAPGRAUT',
         'VAPHAILT',
         'VAPDRIZT',
         'MELTPRIST',
         'MELTSNOWT',
         'MELTAGGRT',
         'MELTGRAUT',
         'MELTHAILT',
         'RIMECLDSNOWT',
         'RIMECLDAGGRT',
         'RIMECLDHAILT',
         'RIMECLDGRAUT',
         'RAIN2PRT',
         'RAIN2SNT',
         'RAIN2AGT',
         'RAIN2GRT',
         'RAIN2HAT',
         'AGGRSELFPRIST',
         'AGGRSELFSNOWT',
         'AGGRPRISSNOWT',
         'INUCHOMRT',
         'INUCCONTRT',
         'INUCIFNRT',
         'INUCHAZRT',
         'AGGREGATET',
         'NUCCLDRT',
         'CLD2RAINT'
          ]

    
Proclist_RAMS_mass=list(List_Processes_RAMS_Mass)

RAMS_processes_mass_split=defaultdict(dict)
RAMS_processes_mass_split['VAPCLDT']=['VAPCLDT','E_VAPCLDT']
RAMS_processes_mass_split['VAPRAINT']=['VAPRAINT','E_VAPRAINT']
RAMS_processes_mass_split['VAPPRIST']=['VAPPRIST','E_VAPPRIST']
RAMS_processes_mass_split['VAPSNOWT']=['VAPSNOWT','E_VAPSNOWT']
RAMS_processes_mass_split['VAPAGGRT']=['VAPAGGRT','E_VAPAGGRT']
RAMS_processes_mass_split['VAPGRAUT']=['VAPGRAUT','E_VAPGRAUT']
RAMS_processes_mass_split['VAPHAILT']=['VAPHAILT','E_VAPHAILDT']
RAMS_processes_mass_split['VAPDRIZT']=['VAPDRIZT','E_VAPDRIZT']

Proclist_RAMS_mass_signed=list(Proclist_RAMS_mass).extend(['E_VAPCLDT','E_VAPRAINT','E_VAPPRIST','E_VAPSNOWT','E_VAPAGGRT','E_VAPHAILDT','E_VAPGRAUT','E_VAPDRIZT'])

rams_processes_mass_grouped=[
'VAPLIQ',
'VAPICE',
'MELTICE',
'CLD2RAIN',
'RIMECLD',
'RAIN2ICE',
'ICE2RAIN',
'NUCCLDR',
'NUCICER'
]

Proclist_rams_mass_grouped=list(morrison_processes_mass)

rams_processes_mass_grouped_split=defaultdict(dict)
rams_processes_mass_grouped_split['VAPLIQ']=['E_VAPLIQ','VAPLIQ']
rams_processes_mass_grouped_split['VAPICE']=['E_VAPICE','VAPICE']

Proclist_rams_mass_grouped_signed=list(Proclist_rams_mass_grouped).extend(['E_VAPLIQ','E_VAPICE'])



def load_wrf_variables_signed(filename,variable_list,split_dict,add_coordinates=None,constraint=None,quantity='mixing ratio',
                              absolute_value=False,parallel_pool=None,
                              debug_nproc=None):
    from wrfcube import loadwrfcube, derivewrfcube
    from iris.cube import CubeList
    from copy import deepcopy
#    from iris.analysis.maths import abs
    cubelist_out=CubeList()
    
    if (debug_nproc is not None):
        variable_list=variable_list[1:debug_nproc+1]

    List_signed=list(split_dict.keys())


    add_coordinates_load=deepcopy(add_coordinates)
    if quantity=='volume':
        rho=derivewrfcube(filename,'density',add_coordinates=add_coordinates,constraint=constraint)
    if add_coordinates is not None:
        if 'z' in add_coordinates:   
            cube=loadwrfcube(filename,variable_list[1],add_coordinates=add_coordinates,constraint=constraint)
            z_coord=cube.coord('geopotential_height')
            #p_coord=cube.coord('pressure')
            z_data_dims=cube.coord_dims('geopotential_height')
            add_coordinates_load.remove('z')
    for variable in variable_list:
        logging.debug('loading ' + str(variable))

        if variable in List_signed:
            List_1=split_sign_variable_wrf(filename,variable,
                                       name_pos=split_dict[variable][0],name_neg=split_dict[variable][1],
                                       add_coordinates=add_coordinates_load,constraint=constraint,absolute_value=absolute_value)
            if add_coordinates is not None:
                if 'z' in add_coordinates:
                    for i,variable in enumerate(List_1):
                       variable.add_aux_coord(z_coord,z_data_dims)
                       List_1[i]=variable
            if quantity=='volume':
                for i,variable in enumerate(List_1):
                    name=variable.name()
                    List_1[i]=(rho*variable)
                    List_1[i].rename(name) 
            cubelist_out.extend(List_1)
        else:
            cube=loadwrfcube(filename,variable,add_coordinates=add_coordinates_load,constraint=constraint)
            if absolute_value:
                cube.data=abs(cube.core_data())
            if add_coordinates is not None:
                if 'z' in add_coordinates:
                    cube.add_aux_coord(z_coord,z_data_dims)
            if quantity=='volume':
                cube=cube*rho
            cube.rename(variable)
            cubelist_out.append(cube)
    return cubelist_out

thompson_processes_mass= list(List_Processes_Thompson_Mass)
#thompson_processes_mass_split={}
thompson_processes_number= list(List_Processes_Thompson_Number)
thompson_processes_number_split={}

def calculate_wrf_mp_path(filename,processes=None,microphysics_scheme=None, signed=False,absolute_value=False,constraint=None,
                          add_coordinates=None,quantity='mixing ratio',parallel_pool=None,debug_nproc=None):
    if microphysics_scheme=='morrison':
        if processes=='mass':
            process_list=morrison_processes_mass
            #process_list.remove('PCCN')
            if signed==True:
                split_dict=morrison_processes_mass_split
            else:
                split_dict={}
        elif processes=='number':
            process_list=morrison_processes_number
            if signed==True:
                split_dict='morrison_processes_number_split'
            else:
                split_dict={}    



        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,absolute_value=absolute_value,
                                                add_coordinates=add_coordinates,quantity=quantity,
                                                constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc)

    elif microphysics_scheme=='thompson':
        if processes=='mass':
            process_list=thompson_processes_mass
            if signed==True:
                split_dict=thompson_processes_mass_split
            else:
                split_dict={}
        elif processes=='number':
            process_list=thompson_processes_number
            if signed==True:
                split_dict=thompson_processes_number_split
            else:
                split_dict={}
        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,absolute_value=absolute_value,
                                                add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,
                                                debug_nproc=debug_nproc)


    elif microphysics_scheme=='sbmfull':
        if processes=='mass':
            process_list=SBMfull_processes_mass
            if signed==True:
                split_dict=SBMfull_processes_mass_split
            else:
                split_dict={}
        elif processes=='number':
            process_list=SBMfull_processes_number
            if signed==True:
                split_dict=SBMfull_processes_number_split
            else:
                split_dict={}
        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,absolute_value=absolute_value,
                                                add_coordinates=add_coordinates,quantity=quantity,
                                                constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc)
 
    else:
        raise ValueError("Unknown microphysics_scheme")

 
    return cube_list_out


def load_rams_variables_signed(filename,variable_list,split_dict,
                               add_coordinates=None,constraint=None,
                               quantity='mixing ratio',accumulated=True,
                               dt_out=None,
                               absolute_value=False,
                               parallel_pool=None,
                               debug_nproc=None):
    from ramscube import loadramscube, deriveramscube
    from iris.cube import CubeList
    from copy import deepcopy
    cubelist_out=CubeList()
    
    if (debug_nproc is not None):
        variable_list=variable_list[1:debug_nproc+1]

    List_signed=list(split_dict.keys())

    if quantity=='volume':
        rho=deriveramscube(filename,'air_density',add_coordinates=add_coordinates,constraint=constraint)    
        
    add_coordinates_load=deepcopy(add_coordinates)

    for variable in variable_list:
        logging.debug('loading '+ str(variable))

        if variable in List_signed:
            List_1=split_sign_variable_rams(filename,variable,
                                       name_pos=split_dict[variable][0],name_neg=split_dict[variable][1],
                                       add_coordinates=add_coordinates_load,constraint=constraint)
            if quantity=='volume':
                for i,variable in enumerate(List_1):
                    name=variable.name()
                    List_1[i]=(rho*variable)
                    List_1[i].rename(name) 
            cubelist_out.extend(List_1)
        else:
            cube=loadramscube(filename,variable,add_coordinates=add_coordinates_load,constraint=constraint)
            cube.data=abs(cube.core_data())
            if quantity=='volume':
                cube=cube*rho
            cube.rename(variable)
            cubelist_out.append(cube)
        if not accumulated:
            for cube in cubelist_out:
                cube=cube/dt_out
            
    return cubelist_out


def calculate_rams_mp_path(filename,processes=None,microphysics_scheme=None,
                           signed=False,constraint=None,add_coordinates=None,
                           quantity='mixing ratio',accumulated='False',
                           parallel_pool=None,
                           dt_out=None,
                           debug_nproc=None):
    from iris.coords import AuxCoord
    if microphysics_scheme=='rams':
        if processes=='mass_grouped':
            process_list=rams_processes_mass_grouped
            #process_list.remove('PCCN')
            if signed==True:
                split_dict=rams_processes_mass_grouped_split
            else:
                split_dict={}        
            cube_list_out=load_rams_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc)

        elif processes=='mass':
            process_list=List_Processes_RAMS_Mass
            #process_list.remove('PCCN')
            if signed==True:
                split_dict=RAMS_processes_mass_split
            else:
                split_dict={}
            cube_list_out=load_rams_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc)
            time_coord=cube_list_out[0].coord('time')
            dt=(time_coord.units.num2date(time_coord.points[1])-time_coord.units.num2date(time_coord.points[0])).total_seconds()
            dt_coord=AuxCoord(dt,units='s')
            for i,process in enumerate(cube_list_out):
                cube_list_out[i]=process/dt_coord
                cube_list_out[i].rename(process.name())

        # elif processes=='number':
        #     process_list=morrison_processes_number
        #     if signed==True:
        #         split_dict='morrison_processes_number_split'
        #     else:
        #         split_dict={}    

 

    else:
        raise ValueError("Unknown microphysics_scheme")

 
    return cube_list_out

def processes_colors(microphysics_scheme=None,colors_processes='all'):
    Processes_signed_colors={}
    Processes_signed_names={}

    if microphysics_scheme=='morrison':
        
        if colors_processes=='lumped':
            Processes_signed_colors=lumped_colors_morrison
            Processes_signed_names=lumped_names_morrison

        if colors_processes=='all':
            Processes_signed_colors['PRC']='brown'       
            Processes_signed_names['PRC']='PRC'         

            Processes_signed_colors['PRD']='lightseagreen'
            Processes_signed_names['PRD']='PRD'

            Processes_signed_colors['PCCN']='blue'
            Processes_signed_names['PCCN']='PCCN'

            Processes_signed_colors['PSMLT']='darkblue'
            Processes_signed_names['PSMLT']='PSMLT'

            Processes_signed_colors['EVPMS']='azure'
            Processes_signed_names['EVPMS']='EVPMS'

            Processes_signed_colors['QMULTS']='cyan'
            Processes_signed_names['QMULTS']='QMULTS'

            Processes_signed_colors['QMULTR']='green'
            Processes_signed_names['QMULTR']='QMULTR'

            Processes_signed_colors['PRACS']='darkgreen'
            Processes_signed_names['PRACS']='PRACS'

            Processes_signed_colors['PGSACW']='gray'
            Processes_signed_names['PGSACW']='PGSACW'

            Processes_signed_colors['PRDG']='springgreen'
            Processes_signed_names['PRDG']='PRDG'

            Processes_signed_colors['EPRDG']='coral'
            Processes_signed_names['EPRDG']='EPRDG'

            Processes_signed_colors['EVPMG']='mediumseagreen'
            Processes_signed_names['EVPMG']='EVPMG'

            Processes_signed_colors['PGMLT']='mediumpurple'
            Processes_signed_names['PGMLT']='PGMLT'

            Processes_signed_colors['PRACI']='lightsteelblue'
            Processes_signed_names['PRACI']='PRACI'

            Processes_signed_colors['PIACRS']='darkslategrey'
            Processes_signed_names['PIACRS']='PIACRS'

            Processes_signed_colors['PRACIS']='skyblue'
            Processes_signed_names['PRACIS']='PRACIS'

            Processes_signed_colors['EPRD']='beige'
            Processes_signed_names['EPRD']='EPRD'

            Processes_signed_colors['PRACG']='violet'
            Processes_signed_names['PRACG']='PRACG'

            Processes_signed_colors['QMULTG']='pink'
            Processes_signed_names['QMULTG']='QMULTG'

            Processes_signed_colors['QMULTRG']='indigo'
            Processes_signed_names['QMULTRG']='QMULTRG'

            Processes_signed_colors['MNUCCR']='lightcyan'
            Processes_signed_names['MNUCCR']='MNUCCR'

            Processes_signed_colors['MNUCCC']='indigo'
            Processes_signed_names['MNUCCC']='MNUCCC'

            Processes_signed_colors['MNUCCD']='indigo'
            Processes_signed_names['MNUCCD']='MNUCCD'

            Processes_signed_colors['PRAI']='lime'
            Processes_signed_names['PRAI']='PRAI'

            Processes_signed_colors['PRCI']='peru'
            Processes_signed_names['PRCI']='PRCI'

            Processes_signed_colors['PSACWS']='maroon'
            Processes_signed_names['PSACWS']='PSACWS'

            Processes_signed_colors['PIACR']='black'
            Processes_signed_names['PIACR']='PIACR'

            Processes_signed_colors['PSACWI']='gold'
            Processes_signed_names['PSACWI']='PSACWI'

            Processes_signed_colors['PSACR']='lightgray'
            Processes_signed_names['PSACR']='PSACR'
                
            Processes_signed_colors['QICF']='#99d8c9'
            Processes_signed_names['QICF']='QICF'

            Processes_signed_colors['QGRF']='#756bb1'
            Processes_signed_names['QGRF']='QGRF'

            Processes_signed_colors['QNIRF']='#bcbddc'
            Processes_signed_names['QNIRF']='QNIRF'
            
            Processes_signed_colors['QIIM']='#d95f0e'
            Processes_signed_names['QIIM']='QIIM'

            # names that are properly set...

            Processes_signed_colors['PCC']='lightblue'        
            Processes_signed_names['PCC']='Cond. droplets (PCC)'
    
            Processes_signed_colors['EPCC']='lightsalmon'
            Processes_signed_names['EPCC']='Evap droplets (EPCC)'
    
            Processes_signed_colors['PRE']='salmon'
            Processes_signed_names['PRE']='Evap. rain (PRE)'#''
            
            Processes_signed_colors['PRA']='lightgreen'
            Processes_signed_names['PRA']='Accretion (PRA)'#''
            
            Processes_signed_colors['PRC']='brown'         
            Processes_signed_names['PRC']='Autoconversion (PRC)'         
    
            Processes_signed_colors['PRDG']='cyan'
            Processes_signed_names['PRDG']='Dep. graupel (PRDG)'#''
    
            Processes_signed_colors['EPRDG']='gold'
            Processes_signed_names['EPRDG']='Subl. graupel (EPRDG)'#''
    
            Processes_signed_colors['EPRD']='khaki'
            Processes_signed_names['EPRD']='Subl. ice (EPRD)'# ''
    
            Processes_signed_colors['EPRDS']='wheat'
            Processes_signed_names['EPRDS']='Subl. snow (EPRDS)'#''
    
            Processes_signed_colors['PGRACS']='orange'
            Processes_signed_names['PGRACS']='Coll. rain/snow (PGRACS)'# ''
    
            Processes_signed_colors['PRDS']='darkorange'
            Processes_signed_names['PRDS']='Dep. snow (PRDS)'#'Dep. snow'
    
            Processes_signed_colors['PSACWG']='palegreen'
            Processes_signed_names['PSACWG']='Coll. droplets/graupel (PSACWG)'#'Coll. droplets/graupel'
    



    elif microphysics_scheme=='thompson':
        
        
        if colors_processes=='lumped':
            Processes_signed_colors=lumped_colors_thompson
            Processes_signed_names=lumped_names_thompson

        if colors_processes=='all':        
            Processes_signed_colors['PRR_RCI']='magenta'   #  Vapor->Water
            Processes_signed_names['PRR_RCI']='PRR_RCI'   #  Vapor->Water

            Processes_signed_colors['PRR_WAU']='salmon'   #  Vapor->Water
            Processes_signed_names['PRR_WAU']='PRR_WAU'   #  Vapor->Water

            Processes_signed_colors['PRR_RCS']='cyan'   #  Vapor->Water
            Processes_signed_names['PRR_RCS']='PRR_RCS'   #  Vapor->Water

            Processes_signed_colors['PRR_RCG']='khaki'   #  Rain->Graupel
            Processes_signed_names['PRR_RCG']='PRR_RCG'   #  Rain->Graupel

            Processes_signed_colors['PRI_IHM']='darkorange'   #  Vapor->Water
            Processes_signed_names['PRI_IHM']='PRI_IHM'   #  Vapor->Water

            Processes_signed_colors['PRI_RFZ']='orange'   #  Vapor->Water
            Processes_signed_names['PRI_RFZ']='PRI_RFZ'   #  Vapor->Water

            Processes_signed_colors['PRI_RCI']='darkblue'   #  Vapor->Water
            Processes_signed_names['PRI_RCI']='PRI_RCI'   #  Vapor->Water

            Processes_signed_colors['PRI_IHA']='azure'   #  Vapor->Water
            Processes_signed_names['PRI_IHA']='PRI_IHA'   #  Vapor->Water

            Processes_signed_colors['PRS_SCI']='coral'   #  Vapor->Water
            Processes_signed_names['PRS_SCI']='PRS_SCI'   #  Vapor->Water

            Processes_signed_colors['PRS_RCS']='mediumseagreen'   #  Vapor->Water
            Processes_signed_names['PRS_RCS']='PRS_RCS'   #  Vapor->Water

            Processes_signed_colors['PRS_SCW']='mediumpurple'   #  Vapor->Water
            Processes_signed_names['PRS_SCW']='PRS_SCW'   #  Vapor->Water

            Processes_signed_colors['PRS_IHM']='skyblue'   #  Vapor->Water
            Processes_signed_names['PRS_IHM']='PRS_IHM'   #  Vapor->Water

            Processes_signed_colors['PRS_IDE']='beige'   #  Vapor->Water
            Processes_signed_names['PRS_IDE']='PRS_IDE'   #  Vapor->Water

            Processes_signed_colors['PRG_SCW']='violet'   #  Vapor->Water
            Processes_signed_names['PRG_SCW']='PRG_SCW'   #  Vapor->Water

            Processes_signed_colors['PRG_RFZ']='pink'   #  Vapor->Water
            Processes_signed_names['PRG_RFZ']='PRG_RFZ'   #  Vapor->Water

            Processes_signed_colors['PRG_GCW']='lightcyan'   #  Vapor->Water
            Processes_signed_names['PRG_GCW']='PRG_GCW'   #  Vapor->Water

            Processes_signed_colors['PRG_RCI']='lime'   #  Vapor->Water
            Processes_signed_names['PRG_RCI']='PRG_RCI'   #  Vapor->Water

            Processes_signed_colors['PRG_RCS']='peru'   #  Vapor->Water
            Processes_signed_names['PRG_RCS']='PRG_RCS'   #  Vapor->Water

            Processes_signed_colors['PRG_IHM']='violet'   #  Graupel->Ice
            Processes_signed_names['PRG_IHM']='PRG_IHM'   #  Graupel->Ice

            Processes_signed_colors['E_PRR_RCS']='pink'   #  Graupel->Ice
            Processes_signed_names['E_PRR_RCS']='E_PRR_RCS'   #  Graupel->Ice

            Processes_signed_colors['E_PRR_RCG']='yellow'   #  Graupel->Ice
            Processes_signed_names['E_PRR_RCG']='E_PRR_RCG'   #  Graupel->Ice

            Processes_signed_colors['E_PRI_IDE']='red'   #  Graupel->Ice
            Processes_signed_names['E_PRI_IDE']='E_PRI_IDE'   #  Graupel->Ice

            Processes_signed_colors['E_PRS_RCS']='green'   #  Graupel->Ice
            Processes_signed_names['E_PRS_RCS']='E_PRS_RCS'   #  Graupel->Ice

            Processes_signed_colors['E_PRG_GDE']='gold'   #  Graupel->Ice
            Processes_signed_names['E_PRG_GDE']='E_PRG_GDE'   #  Graupel->Ice

            Processes_signed_colors['PRI_WFI']='maroon'   #  Graupel->Ice
            Processes_signed_names['PRI_WFI']='PRI_WFI'   #  Graupel->Ice
            
            Processes_signed_colors['PRW_IMI']='maroon'   #  Graupel->Ice
            Processes_signed_names['PRW_IMI']='PRW_IMI'   #  Graupel->Ice
            
            # names that are properly set:
            Processes_signed_colors['PRI_INU']='lightseagreen'   
            Processes_signed_names['PRI_INU']='Ice nucleation (PRI_INU)'   
    
            Processes_signed_colors['PRR_RCW']='lightgreen'  
            Processes_signed_names['PRR_RCW']='Coll. droplets/rain (PRR_RCW)'  
    
            Processes_signed_colors['PRR_GML']='wheat'  
            Processes_signed_names['PRR_GML']='Melt. graupel (PRR_GML)' 
    
            Processes_signed_colors['PRI_IDE']='blue'   
            Processes_signed_names['PRI_IDE']='Dep. ice (PRI_IDE)'   
    
            Processes_signed_colors['PRS_SDE']='lightsteelblue' 
            Processes_signed_names['PRS_SDE']='Dep. snow (PRS_SDE)'
            
            Processes_signed_colors['PRS_IAU']='green'   
            Processes_signed_names['PRS_IAU']='Autoconv.ice (PRS_IAU)'   
    
            Processes_signed_colors['PRI_WFZ']='darkred'  
            Processes_signed_names['PRI_WFZ']='Freez. droplets (PRI_WFZ)'   
    
            Processes_signed_colors['PRG_GDE']='indigo'   
            Processes_signed_names['PRG_GDE']='Dep. graupel (PRG_GDE)'   
    
            Processes_signed_colors['E_PRS_SDE']='darkslateblue'  
            Processes_signed_names['E_PRS_SDE']='Subl. snow (E_PRS_SDE)'  
    
            Processes_signed_colors['PRG_RCG']='black'  
            Processes_signed_names['PRG_RCG']='Coll. rain/graupel (PRG_RCG)'
    
            Processes_signed_colors['PRV_REV']='lightsalmon'   #  Vapor->Water
            Processes_signed_names['PRV_REV']='Evaporation of rain (PRV_REV)'
    
            Processes_signed_colors['PRW_VCD']='lightblue'   #  Vapor->Water
            Processes_signed_names['PRW_VCD']='Condensation (PRW_VCD)'
    
            Processes_signed_colors['E_PRW_VCD']='coral'   #  Vapor->Water
            Processes_signed_names['E_PRW_VCD']='Evaporation (E_PRW_VCD)'


    elif microphysics_scheme=='rams':
        if colors_processes=='lumped':
            Processes_signed_colors=lumped_colors_rams
            Processes_signed_names=lumped_names_rams

    else:
        raise ValueError('unknown microphysics_scheme '+str(microphysics_scheme)+ ', must be morrison, thompson or rams')
    return(Processes_signed_colors,Processes_signed_names)

color_condensation=   '#4b86c2'   #  bright blue
color_evaporation=    '#ffd633'   #  yellow
color_freezing=       '#002266'   #  dark blue
color_dropletfreezing='#7d86fb'   #  bright cornflower blue
color_rainfreezing=   '#0000B2'   #  blue
color_riming=         '#7647A2'   #  purple
color_dropletriming=  '#AA8CC5'   #  purple
color_rainriming=     '#7647A2'   #  purple
color_melting=        '#ff9a00'   #  orange
color_deposition=     '#34dabe'   #  cyan
color_graupeldeposition= '#004c4c'   #  darkcyan
color_icedeposition=     '#99ffff'   #  lightcyan
color_snowdeposition=    '#009999'   #  mediumcyan
color_sublimation=    '#FBA69C'   #  salmon
color_graupelsublimation=    '#964c44'   #  darksalmon
color_icesublimation=    '#fcbfb8'   #  lightsalmon
color_snowsublimation=    '#e17366'   #  mediumsalmon

color_ice=            '#D4F0FF'   #  icy blue
color_warmrain=       '#90db26'   #  green
color_autoconversion= '#007F00'   #  darkgreen
color_accretion=      '#9CBC36'   #  lightgreen



list_lumped_names_morrison=[]
list_lumped_processes_morrison=[]
lumped_colors_morrison={}
lumped_names_morrison={}

list_lumped_names_morrison.append('Condensation')
list_lumped_processes_morrison.append(['PCC','PCCN'])
lumped_colors_morrison['Condensation']=color_condensation
lumped_names_morrison['Condensation']='Condensation'

list_lumped_names_morrison.append('Evaporation')
list_lumped_processes_morrison.append(['EPCC','PRE'])
lumped_colors_morrison['Evaporation']=color_evaporation
lumped_names_morrison['Evaporation']='Evaporation'

list_lumped_names_morrison.append('Freezing')
list_lumped_processes_morrison.append(['MNUCCC','MNUCCR','MNUCCD','PSACWS','PSACWI','PIACR','QMULTG','QMULTRG','QMULTS','PRACS','PIACRS','QMULTR','PSACWG','PGRACS','PRACG','PGSACW','QICF','QGRF','QNIRF'])
lumped_colors_morrison['Freezing']=color_freezing
lumped_names_morrison['Freezing']='Freezing'

list_lumped_names_morrison.append('Pure Freezing')
list_lumped_processes_morrison.append(['MNUCCC','MNUCCR','MNUCCD','QICF','QGRF','QNIRF'])
lumped_colors_morrison['Pure Freezing']=color_freezing
lumped_names_morrison['Pure Freezing']='Freezing'

list_lumped_names_morrison.append('Droplet Freezing')
list_lumped_processes_morrison.append(['MNUCCC','MNUCCD','QICF'])
lumped_colors_morrison['Droplet Freezing']=color_dropletfreezing
lumped_names_morrison['Droplet Freezing']='Droplet Freezing'

list_lumped_names_morrison.append('Rain Freezing')
list_lumped_processes_morrison.append(['MNUCCR','QGRF','QNIRF'])
lumped_colors_morrison['Rain Freezing']=color_rainfreezing
lumped_names_morrison['Rain Freezing']='Rain Freezing'

list_lumped_names_morrison.append('Riming')
list_lumped_processes_morrison.append(['PSACWS','PSACWI','PIACR','QMULTG','QMULTS','PRACS','QMULTR','QMULTRG','PSACWG','PGRACS','PIACRS','PRACG','PGSACW'])
lumped_colors_morrison['Riming']=color_riming
lumped_names_morrison['Riming']='Riming'

list_lumped_names_morrison.append('Droplet Riming')
list_lumped_processes_morrison.append(['PSACWS','PSACWI','QMULTG','QMULTS','PSACWG','PGSACW'])
lumped_colors_morrison['Droplet Riming']=color_dropletriming
lumped_names_morrison['Droplet Riming']='Droplet Riming'

list_lumped_names_morrison.append('Rain Riming')
list_lumped_processes_morrison.append(['PIACR','PRACS','QMULTR','QMULTRG','PGRACS','PRACG','PIACRS'])
lumped_colors_morrison['Rain Riming']=color_rainriming
lumped_names_morrison['Rain Riming']='Rain Riming'

list_lumped_names_morrison.append('Melting')
list_lumped_processes_morrison.append(['PSMLT','PGMLT','QIIM'])
lumped_colors_morrison['Melting']=color_melting
lumped_names_morrison['Melting']='Melting'

list_lumped_names_morrison.append('Melting to Rain')
list_lumped_processes_morrison.append(['PSMLT','PGMLT'])
lumped_colors_morrison['Melting to Rain']=color_melting
lumped_names_morrison['Melting to Rain']='Melting to Rain'

list_lumped_names_morrison.append('Rain formation')
list_lumped_processes_morrison.append(['PRC','PRA'])
lumped_colors_morrison['Rain formation']=color_warmrain
lumped_names_morrison['Rain formation']='Rain formation'

list_lumped_names_morrison.append('Autoconversion')
list_lumped_processes_morrison.append(['PRC'])
lumped_colors_morrison['Autoconversion']=color_autoconversion
lumped_names_morrison['Autoconversion']='Autoconversion'

list_lumped_names_morrison.append('Accretion')
list_lumped_processes_morrison.append(['PRA'])
lumped_colors_morrison['Accretion']=color_accretion
lumped_names_morrison['Accretion']='Accretion'

list_lumped_names_morrison.append('Deposition')
list_lumped_processes_morrison.append(['PRD','PRDS','PRDG','MNUCCD'])
lumped_colors_morrison['Deposition']=color_deposition
lumped_names_morrison['Deposition']='Deposition'

list_lumped_names_morrison.append('Graupel Deposition')
list_lumped_processes_morrison.append(['PRDG'])
lumped_colors_morrison['Graupel Deposition']=color_graupeldeposition
lumped_names_morrison['Graupel Deposition']='Graupel Deposition'

list_lumped_names_morrison.append('Ice Deposition')
list_lumped_processes_morrison.append(['PRD','MNUCCD'])
lumped_colors_morrison['Ice Deposition']=color_icedeposition
lumped_names_morrison['Ice Deposition']='Ice Deposition'

list_lumped_names_morrison.append('Snow Deposition')
list_lumped_processes_morrison.append(['PRDS'])
lumped_colors_morrison['Snow Deposition']=color_snowdeposition
lumped_names_morrison['Snow Deposition']='Snow Deposition'

list_lumped_names_morrison.append('Sublimation')
list_lumped_processes_morrison.append(['EPRD','EPRDS','EPRDG','EVPMS','EVPMG'])
lumped_colors_morrison['Sublimation']=color_sublimation
lumped_names_morrison['Sublimation']='Sublimation'

list_lumped_names_morrison.append('Graupel Sublimation')
list_lumped_processes_morrison.append(['EPRDG','EVPMG'])
lumped_colors_morrison['Graupel Sublimation']=color_graupelsublimation
lumped_names_morrison['Graupel Sublimation']='Graupel Sublimation'

list_lumped_names_morrison.append('Ice Sublimation')
list_lumped_processes_morrison.append(['EPRD'])
lumped_colors_morrison['Ice Sublimation']=color_icesublimation
lumped_names_morrison['Ice Sublimation']='Ice Sublimation'

list_lumped_names_morrison.append('Snow Sublimation')
list_lumped_processes_morrison.append(['EPRDS','EVPMS'])
lumped_colors_morrison['Snow Sublimation']=color_snowsublimation
lumped_names_morrison['Snow Sublimation']='Snow Sublimation'
#
list_lumped_names_morrison.append('Ice processes')
list_lumped_processes_morrison.append(['PRAI','PRCI','PRACIS','PSACR','PRACI'])
lumped_colors_morrison['Ice processes']=color_ice
lumped_names_morrison['Ice processes']='Ice processes'

#lumped_colors_morrison['Other']='grey'


# Thompson Microphysics:
list_lumped_names_thompson=[]
list_lumped_processes_thompson=[]
lumped_colors_thompson={}
lumped_names_thompson={}

list_lumped_names_thompson.append('Condensation')
list_lumped_processes_thompson.append(['PRW_VCD'])
lumped_colors_thompson['Condensation']=color_condensation
lumped_names_thompson['Condensation']='Condensation'

list_lumped_names_thompson.append('Evaporation')
list_lumped_processes_thompson.append(['E_PRW_VCD','PRV_REV'])
lumped_colors_thompson['Evaporation']=color_evaporation
lumped_names_thompson['Evaporation']='Evaporation'

list_lumped_names_thompson.append('Freezing')
list_lumped_processes_thompson.append(['PRG_RFZ','PRI_WFZ','PRI_RFZ','PRR_RCG','PRG_GCW','PRG_SCW','PRS_SCW','PRR_RCS','PRR_RCI','PRI_WFI'])
lumped_colors_thompson['Freezing']=color_freezing
lumped_names_thompson['Freezing']='Freezing'

list_lumped_names_thompson.append('Pure Freezing')
list_lumped_processes_thompson.append(['PRG_RFZ','PRI_WFZ','PRI_RFZ','PRI_WFI'])
lumped_colors_thompson['Pure Freezing']=color_freezing
lumped_names_thompson['Pure Freezing']='Freezing'

list_lumped_names_thompson.append('Droplet Freezing')
list_lumped_processes_thompson.append(['PRI_WFZ','PRI_WFI'])
lumped_colors_thompson['Droplet Freezing']=color_dropletfreezing
lumped_names_thompson['Droplet Freezing']='Droplet Freezing'

list_lumped_names_thompson.append('Rain Freezing')
list_lumped_processes_thompson.append(['PRG_RFZ','PRI_RFZ'])
lumped_colors_thompson['Rain Freezing']=color_rainfreezing
lumped_names_thompson['Rain Freezing']='Rain Freezing'

list_lumped_names_thompson.append('Riming')
list_lumped_processes_thompson.append(['PRG_GCW','PRG_SCW','PRS_SCW','E_PRR_RCG','E_PRR_RCS','PRR_RCI'])
lumped_colors_thompson['Riming']=color_riming
lumped_names_thompson['Riming']='Riming'

list_lumped_names_thompson.append('Droplet Riming')
list_lumped_processes_thompson.append(['PRG_GCW','PRG_SCW','PRS_SCW'])
lumped_colors_thompson['Droplet Riming']=color_dropletriming
lumped_names_thompson['Droplet Riming']='Droplet Riming'

list_lumped_names_thompson.append('Rain Riming')
list_lumped_processes_thompson.append(['E_PRR_RCG','E_PRR_RCS','PRR_RCI'])
lumped_colors_thompson['Rain Riming']=color_rainriming
lumped_names_thompson['Rain Riming']='Rain Riming'

list_lumped_names_thompson.append('Melting')
list_lumped_processes_thompson.append(['PRR_GML', 'PRW_IMI','PRR_SML','PRR_RCG','PRR_RCS'])
lumped_colors_thompson['Melting']=color_melting
lumped_names_thompson['Melting']='Melting'

list_lumped_names_thompson.append('Melting to Rain')
list_lumped_processes_thompson.append(['PRR_GML','PRR_SML','PRR_RCG','PRR_RCS'])
lumped_colors_thompson['Melting to Rain']=color_melting
lumped_names_thompson['Melting to Rain']='Melting'

list_lumped_names_thompson.append('Rain formation')
list_lumped_processes_thompson.append(['PRR_WAU','PRR_RCW'])
lumped_colors_thompson['Rain formation']=color_warmrain
lumped_names_thompson['Rain formation']='Rain formation'

list_lumped_names_thompson.append('Autoconversion')
list_lumped_processes_thompson.append(['PRR_WAU'])
lumped_colors_thompson['Autoconversion']=color_autoconversion
lumped_names_thompson['Autoconversion']='Autoconversion'

list_lumped_names_thompson.append('Accretion')
list_lumped_processes_thompson.append(['PRR_RCW'])
lumped_colors_thompson['Accretion']=color_accretion
lumped_names_thompson['Accretion']='Accretion'

list_lumped_names_thompson.append('Deposition')
list_lumped_processes_thompson.append(['PRG_GDE','PRS_SDE','PRI_IDE','PRS_IDE','PRI_INU','PRI_IHA'])
lumped_colors_thompson['Deposition']=color_deposition
lumped_names_thompson['Deposition']='Deposition'

list_lumped_names_thompson.append('Graupel Deposition')
list_lumped_processes_thompson.append(['PRG_GDE'])
lumped_colors_thompson['Graupel Deposition']=color_graupeldeposition
lumped_names_thompson['Graupel Deposition']='Graupel Deposition'

list_lumped_names_thompson.append('Ice Deposition')
list_lumped_processes_thompson.append(['PRS_IDE','PRI_INU','PRI_IHA'])
lumped_colors_thompson['Ice Deposition']=color_icedeposition
lumped_names_thompson['Ice Deposition']='Ice Deposition'

list_lumped_names_thompson.append('Snow Deposition')
list_lumped_processes_thompson.append(['PRS_SDE'])
lumped_colors_thompson['Snow Deposition']=color_snowdeposition
lumped_names_thompson['Snow Deposition']='Snow Deposition'

list_lumped_names_thompson.append('Sublimation')
list_lumped_processes_thompson.append(['E_PRI_SDE','E_PRS_SDE','E_PRG_GDE'])
lumped_colors_thompson['Sublimation']=color_sublimation
lumped_names_thompson['Sublimation']='Sublimation'

list_lumped_names_thompson.append('Graupel Sublimation')
list_lumped_processes_thompson.append(['E_PRG_GDE'])
lumped_colors_thompson['Graupel Sublimation']=color_graupelsublimation
lumped_names_thompson['Graupel Sublimation']='Graupel Sublimation'

list_lumped_names_thompson.append('Ice Sublimation')
list_lumped_processes_thompson.append(['E_PRS_SDE'])
lumped_colors_thompson['Ice Sublimation']=color_icesublimation
lumped_names_thompson['Ice Sublimation']='Ice Sublimation'

list_lumped_names_thompson.append('Snow Sublimation')
list_lumped_processes_thompson.append(['E_PRI_IDE'])
lumped_colors_thompson['Snow Sublimation']=color_snowsublimation
lumped_names_thompson['Snow Sublimation']='Snow Sublimation'

list_lumped_names_thompson.append('Ice processes')
list_lumped_processes_thompson.append(['PRS_SCI','PRS_IAU','PRI_IHM'])
lumped_colors_thompson['Ice processes']=color_ice
lumped_names_thompson['Ice processes']='Ice processes'

lumped_colors_thompson['Other']='grey'

list_lumped_names_sbmfull=[]
list_lumped_processes_sbmfull=[]
lumped_colors_sbmfull={}

#list_lumped_names_sbmfull.append('Condensation')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Condensation']=color_condensation
#
#list_lumped_names_sbmfull.append('Evaporation')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Evaporation']=color_evaporation
#`
list_lumped_names_sbmfull.append('Freezing')
#list_lumped_processes_sbmfull.append(['P_FRZ_ICE','P_FRZ_HAIL'])
list_lumped_processes_sbmfull.append(['QVAPOR'])

lumped_colors_sbmfull['Freezing']=color_freezing

list_lumped_names_sbmfull.append('Melting')
list_lumped_processes_sbmfull.append(['QCLOUD'])
lumped_colors_sbmfull['Melting']=color_melting

#list_lumped_names_sbmfull.append('Rain formation')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Rain formation']=color_autoconversion
#
#list_lumped_names_sbmfull.append('Deposition')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Deposition']=color_deposition
#
#list_lumped_names_sbmfull.append('Sublimation')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Sublimation']=color_sublimation
#
#list_lumped_names_sbmfull.append('Ice processes')
#list_lumped_processes_sbmfull.append([])
#lumped_colors_sbmfull['Ice processes']=color_ice
#
#lumped_colors_sbmfull['Other']='grey'



list_lumped_names_rams=[]
list_lumped_processes_rams=[]
lumped_colors_rams={}
lumped_names_rams={}

list_lumped_names_rams.append('Condensation')
list_lumped_processes_rams.append(['E_VAPLIQ','NUCCLDR'])
lumped_colors_rams['Condensation']=color_condensation
lumped_names_rams['Condensation']='Condensation'

list_lumped_names_rams.append('Evaporation')
list_lumped_processes_rams.append(['VAPLIQ'])
lumped_colors_rams['Evaporation']=color_evaporation
lumped_names_rams['Evaporation']='Evaporation'

list_lumped_names_rams.append('Freezing')
list_lumped_processes_rams.append(['RIMECLD','RAIN2ICE','NUCICER'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Pure Freezing')
list_lumped_processes_rams.append(['NUCICER'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Droplet Freezing')
list_lumped_processes_rams.append(['NUCICER'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Riming')
list_lumped_processes_rams.append(['RIMECLD','RAIN2ICE','NUCICER'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Droplet Riming')
list_lumped_processes_rams.append(['RIMECLD'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Rain Riming')
list_lumped_processes_rams.append(['RAIN2ICE'])
lumped_colors_rams['Freezing']=color_freezing
lumped_names_rams['Freezing']='Freezing'

list_lumped_names_rams.append('Melting')
list_lumped_processes_rams.append(['MELTICE','ICE2RAIN'])
lumped_colors_rams['Melting']=color_melting
lumped_names_rams['Melting']='Melting'

list_lumped_names_rams.append('Rain formation')
list_lumped_processes_rams.append(['CLD2RAIN'])
lumped_colors_rams['Rain formation']=color_warmrain
lumped_names_rams['Rain formation']='Rain formation'

list_lumped_names_rams.append('Deposition')
list_lumped_processes_rams.append(['E_VAPICE'])
lumped_colors_rams['Deposition']=color_deposition
lumped_names_rams['Deposition']='Deposition'

list_lumped_names_rams.append('Sublimation')
list_lumped_processes_rams.append(['VAPICE'])
lumped_colors_rams['Sublimation']=color_sublimation
lumped_names_rams['Sublimation']='Sublimation'

#lumped_colors_rams['Other']='grey'


list_lumped_names_rams_all=[]
list_lumped_processes_rams_all=[]
lumped_colors_rams_all={}
lumped_names_rams_all={}

list_lumped_names_rams_all.append('Condensation')
list_lumped_processes_rams_all.append(['E_VAPLIQT','NUCCLDRT'])
lumped_colors_rams_all['Condensation']=color_condensation
lumped_names_rams_all['Condensation']='Condensation'

list_lumped_names_rams_all.append('Evaporation')
list_lumped_processes_rams_all.append(['VAPLIQT'])
lumped_colors_rams_all['Evaporation']=color_evaporation
lumped_names_rams_all['Evaporation']='Evaporation'

list_lumped_names_rams_all.append('Freezing')
list_lumped_processes_rams_all.append(['RIMECLDT','RAIN2ICET','NUCICERT'])
lumped_colors_rams_all['Freezing']=color_freezing
lumped_names_rams_all['Freezing']='Freezing'

list_lumped_names_rams_all.append('Melting')
list_lumped_processes_rams_all.append(['MELTICET','ICE2RAINT'])
lumped_colors_rams_all['Melting']=color_melting
lumped_names_rams_all['Melting']='Melting'

list_lumped_names_rams_all.append('Rain formation')
list_lumped_processes_rams_all.append(['CLD2RAINT'])
lumped_colors_rams_all['Rain formation']=color_autoconversion
lumped_names_rams_all['Rain formation']='Rain formation'

list_lumped_names_rams_all.append('Deposition')
list_lumped_processes_rams_all.append(['E_VAPICET'])
lumped_colors_rams_all['Deposition']=color_deposition
lumped_names_rams_all['Deposition']='Deposition'

list_lumped_names_rams_all.append('Sublimation')
list_lumped_processes_rams_all.append(['VAPICET'])
lumped_colors_rams_all['Sublimation']=color_sublimation
lumped_names_rams_all['Sublimation']='Sublimation'

#lumped_colors_rams['Other']='grey'



def lump_cubelist(cubelist_in,list_names_in, list_cubes_in,lumping='basic'):#,others=False):
    from iris.cube import CubeList
    if lumping=='basic':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Condensation','Evaporation','Freezing','Melting','Deposition','Sublimation','Rain formation']:
                list_names.append(list_names_in[i])
                list_cubes.append(list_cubes_in[i])

    if lumping=='latent':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Condensation','Evaporation','Freezing','Melting','Deposition','Sublimation']:
                list_names.append(list_names_in[i])
                list_cubes.append(list_cubes_in[i])

    if lumping=='detailed':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Condensation','Evaporation',
                        'Freezing','Pure Freezing','Droplet Freezing','Rain Freezing','Riming','Droplet Riming','Rain Riming',
                        'Melting','Melting to Rain',
                        'Deposition','Ice Deposition','Snow Deposition','Graupel Deposition',
                        'Sublimation','Ice Sublimation','Snow Sublimation','Graupel Sublimation',
                        'Rain formation','Autoconversion','Accretion','Ice processes']:
                list_names.append(list_names_in[i])
                list_cubes.append(list_cubes_in[i])

    
    cubelist_out=CubeList()
    list_cubes_other=[cube.name() for cube in cubelist_in]
    for i,name in enumerate(list_names):
        cubelist=cubelist_in.extract(list_cubes[i])
        if cubelist:
            cube=sum(cubelist)
            cube.rename(name)        
            cubelist_out.append(cube)
        #Remove these list_cubes from "Other"
        list_cubes_other=list(set(list_cubes_other)-set(list_cubes[i]))
    # #Add allremaining list_cubes and call them "other"
    # if others:
    #     cubelist=cubelist_in.extract(list_cubes_other)
    #     if cubelist:
    #         cube=sum(cubelist)
    #         cube.rename('Other')
    #         cubelist_out.append(cube)

    return cubelist_out


def lump_processes(processes_in,microphysics_scheme=None,lumping='basic'):#,others=True):
    if (microphysics_scheme=='morrison'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_morrison, list_lumped_processes_morrison,lumping=lumping)#,others=others)
    elif (microphysics_scheme=='thompson'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_thompson, list_lumped_processes_thompson,lumping=lumping)#,others=others)
    elif (microphysics_scheme=='sbmfull'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_sbmfull, list_lumped_processes_sbmfull,lumping=lumping)#,others=others)
    elif (microphysics_scheme=='rams'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_rams, list_lumped_processes_rams,lumping=lumping)#,others=others)
    else:
        raise ValueError('microphysics must be morrison, thompson, sbmfull or rams')
    return processes_out


def lumped_latentheating(processes_in,microphysics_scheme=None):
    from iris.cube import CubeList
    from iris.coords import AuxCoord
    cubelist_out=CubeList()
    SLH_fusion = AuxCoord(334e3,long_name='specific latent heat of fusion', units='joules per kilogram')
    SLH_vaporisation = AuxCoord(2.26476e6,long_name='specific latent heat of vaporisation', units='joules per kilogram')
    SLH_fusion_vaporisation = AuxCoord(334e3+2.26476e6,long_name='specific latent heat of fusion and vaporisation', units='joules per kilogram')


    lumped_processes=lump_processes(processes_in,microphysics_scheme=microphysics_scheme,lumping='latent')#,others=False)
    for cube in lumped_processes:
        name=cube.name()
        if name=='Condensation':
            cube=cube*SLH_vaporisation
        if name=='Evaporation':
            cube=cube*(-1)*SLH_vaporisation
        if name=='Freezing':
            cube=cube*SLH_fusion
        if name=='Melting':
            cube=cube*(-1)*SLH_fusion
        if name=='Deposition':
            cube=cube*1*(SLH_fusion_vaporisation)
        if name=='Sublimation':
            cube=cube*(-1)*(SLH_fusion_vaporisation) 
        cube.rename(name)
        cubelist_out.append(cube)
    return cubelist_out


def lumped_latentheatingmass(lumped_processes):
    from iris.cube import CubeList
    from iris.coords import AuxCoord
    cubelist_out=CubeList()
    SLH_fusion = AuxCoord(334e3,long_name='specific latent heat of fusion', units='joules per kilogram')
    SLH_vaporisation = AuxCoord(2.26476e6,long_name='specific latent heat of vaporisation', units='joules per kilogram')
    SLH_fusion_vaporisation = AuxCoord(334e3+2.26476e6,long_name='specific latent heat of fusion and vaporisation', units='joules per kilogram')

    for cube in lumped_processes:
        name=cube.name()
        if (name =='Rain formation' or name =='Ice processes'):
           cube=cube*SLH_fusion
        if name=='Condensation':
            cube=cube*SLH_vaporisation
        if name=='Evaporation':
            cube=cube*(-1)*SLH_vaporisation
        if name=='Freezing':
            cube=cube*SLH_fusion
        if name=='Melting':
            cube=cube*(-1)*SLH_fusion
        if name=='Deposition':
            cube=cube*1*(SLH_fusion_vaporisation)
        if name=='Sublimation':
            cube=cube*(-1)*(SLH_fusion_vaporisation) 
        cube.rename(name)
        cubelist_out.append(cube)
    return cubelist_out

    
def latentheating_grouped(lumped_latentheating):
    from iris.cube import CubeList
    cubelist_out=CubeList()
    LHRFRZ=lumped_latentheating.extract_strict('Melting')+lumped_latentheating.extract_strict('Freezing')
    LHRFRZ.rename('LHRFRZ')
    LHREVP=lumped_latentheating.extract_strict('Condensation')+lumped_latentheating.extract_strict('Evaporation')
    LHREVP.rename('LHREVP')
    LHRSUB=lumped_latentheating.extract_strict('Sublimation')+lumped_latentheating.extract_strict('Deposition')
    LHRSUB.rename('LHRSUB')
    cubelist_out.extend([LHRFRZ,LHREVP,LHRSUB])
    return cubelist_out

def latentheating_total(lumped_latentheating):
    from iris.cube import CubeList
    cubelist_out=CubeList()
    LHR=lumped_latentheating.extract_strict('Melting')+lumped_latentheating.extract_strict('Freezing')+lumped_latentheating.extract_strict('Condensation')+lumped_latentheating.extract_strict('Evaporation')+lumped_latentheating.extract_strict('Sublimation')+lumped_latentheating.extract_strict('Deposition')
    LHR.rename('latent_heating_rate')
    cubelist_out.append(LHR)
    return cubelist_out 

def load_latent_heating_wrf(filename,microphysics_scheme=None,constraint=None,add_coordinates=None):
    from iris.cube import CubeList
    from wrfcube.wrfcube import variable_list
    from wrfcube import loadwrfcube
    latent=CubeList()
    
    if 'LHREVP' in variable_list(filename):
            
        LHREVP=loadwrfcube(filename,'LHREVP',constraint=constraint,add_coordinates=add_coordinates)
        LHRFRZ=loadwrfcube(filename,'LHRFRZ',constraint=constraint,add_coordinates=add_coordinates)
        LHRSUB=loadwrfcube(filename,'LHRSUB',constraint=constraint,add_coordinates=add_coordinates)
        

        latent.append(LHREVP)
        latent.append(LHRFRZ)
        latent.append(LHRSUB)
        
        latent.extend(split_sign_variable_wrf(filename,'LHREVP',name_neg='latent_heating_rate_of_evaporation',name_pos='latent_heating_rate_of_condensation',add_coordinates=None,constraint=None))
        latent.extend(split_sign_variable_wrf(filename,'LHRFRZ',name_neg='latent_heating_rate_of_melting',name_pos='latent_heating_rate_of_freezing',add_coordinates=None,constraint=None))
        latent.extend(split_sign_variable_wrf(filename,'LHRSUB',name_neg='latent_heating_rate_of_sublimation',name_pos='latent_heating_rate_of_deposition',add_coordinates=None,constraint=None))

    if microphysics_scheme in ["morrison","thompson"]:
        LHR=LHREVP+LHRFRZ+LHRSUB
        LHR.rename('latent_heating_rate')
        latent.append(LHR)

    elif (microphysics_scheme in ["sbmfull"] and 'LHRTOT' in variable_list(filename)):
        LHR=loadwrfcube(filename,'LHRTOT',constraint=constraint,add_coordinates=add_coordinates)
        LHR.rename('latent_heating_rate')
        latent.append(LHR)
        
    return latent

# hydrometeors:
    
color_cloud='firebrick'
color_rain='dodgerblue'
color_drizzle='rebeccapurple'
color_ice='grey'
color_ice1='salmon'
color_ice2='darkseagreen'
color_snow='orange'
color_hail='cyan'
color_graupel='mediumturquoise'
color_aggregate='green'

# WRF Morrison:
list_hydrometeor_variables_morrison=[]
colors_hydrometeors_morrison={}
names_hydrometeors_morrison={}

list_hydrometeor_variables_morrison.append('QCLOUD')
colors_hydrometeors_morrison['QCLOUD']=color_cloud
names_hydrometeors_morrison['QCLOUD']='Cloud droplets'

list_hydrometeor_variables_morrison.append('QRAIN')
colors_hydrometeors_morrison['QRAIN']=color_rain
names_hydrometeors_morrison['QRAIN']='Rain drops'

list_hydrometeor_variables_morrison.append('QICE')
colors_hydrometeors_morrison['QICE']=color_ice
names_hydrometeors_morrison['QICE']='Cloud ice'

list_hydrometeor_variables_morrison.append('QSNOW')
colors_hydrometeors_morrison['QSNOW']=color_snow
names_hydrometeors_morrison['QSNOW']='Snow'

list_hydrometeor_variables_morrison.append('QGRAUP')
colors_hydrometeors_morrison['QGRAUP']=color_graupel
names_hydrometeors_morrison['QGRAUP']='Graupel/Hail'

# WRF Thompson:
list_hydrometeor_variables_thompson=[]
colors_hydrometeors_thompson={}
names_hydrometeors_thompson={}

list_hydrometeor_variables_thompson.append('QCLOUD')
colors_hydrometeors_thompson['QCLOUD']=color_cloud
names_hydrometeors_thompson['QCLOUD']='Cloud droplets'

list_hydrometeor_variables_thompson.append('QRAIN')
colors_hydrometeors_thompson['QRAIN']=color_rain
names_hydrometeors_thompson['QRAIN']='Rain drops'

list_hydrometeor_variables_thompson.append('QICE')
colors_hydrometeors_thompson['QICE']=color_ice
names_hydrometeors_thompson['QICE']='Cloud ice'

list_hydrometeor_variables_thompson.append('QSNOW')
colors_hydrometeors_thompson['QSNOW']=color_snow
names_hydrometeors_thompson['QSNOW']='Snow'

list_hydrometeor_variables_thompson.append('QGRAUP')
colors_hydrometeors_thompson['QGRAUP']=color_graupel
names_hydrometeors_thompson['QGRAUP']='Graupel'

# WRF SBM Full:
list_hydrometeor_variables_sbmfull=[]
colors_hydrometeors_sbmfull={}
names_hydrometeors_sbmfull={}

list_hydrometeor_variables_sbmfull.append('QCLOUD')
colors_hydrometeors_sbmfull['QCLOUD']=color_cloud
names_hydrometeors_sbmfull['QCLOUD']='Cloud droplets'

list_hydrometeor_variables_sbmfull.append('QRAIN')
colors_hydrometeors_sbmfull['QRAIN']=color_rain
names_hydrometeors_sbmfull['QRAIN']='Rain drops'

list_hydrometeor_variables_sbmfull.append('QICEC')
colors_hydrometeors_sbmfull['QICEC']=color_ice
names_hydrometeors_sbmfull['QICEC']='Ice columns'

list_hydrometeor_variables_sbmfull.append('QICED')
colors_hydrometeors_sbmfull['QICED']=color_ice1
names_hydrometeors_sbmfull['QICED']='Cloud dentrites'

list_hydrometeor_variables_sbmfull.append('QICEP')
colors_hydrometeors_sbmfull['QICEP']=color_ice2
names_hydrometeors_sbmfull['QICEP']='Cloud plates'

list_hydrometeor_variables_sbmfull.append('QSNOW')
colors_hydrometeors_sbmfull['QSNOW']=color_snow
names_hydrometeors_sbmfull['QSNOW']='Snow'

list_hydrometeor_variables_sbmfull.append('QGRAUP')
colors_hydrometeors_sbmfull['QGRAUP']=color_graupel
names_hydrometeors_sbmfull['QGRAUP']='Graupel'

list_hydrometeor_variables_sbmfull.append('QHAIL')
colors_hydrometeors_sbmfull['QHAIL']=color_hail
names_hydrometeors_sbmfull['QHAIL']='Hail'

# WRF SBM Fast:
list_hydrometeor_variables_sbmfast=[]
colors_hydrometeors_sbmfast={}
names_hydrometeors_sbmfast={}

list_hydrometeor_variables_sbmfast.append('QCLOUD')
colors_hydrometeors_sbmfast['QCLOUD']=color_cloud
names_hydrometeors_sbmfast['QCLOUD']='Cloud droplets'

list_hydrometeor_variables_sbmfast.append('QRAIN')
colors_hydrometeors_sbmfast['QRAIN']=color_rain
names_hydrometeors_sbmfast['QRAIN']='Rain drops'

list_hydrometeor_variables_sbmfast.append('QICEC')
colors_hydrometeors_sbmfast['QICEC']=color_ice
names_hydrometeors_sbmfast['QICEC']='Ice columns'

list_hydrometeor_variables_sbmfast.append('QICED')
colors_hydrometeors_sbmfast['QICED']=color_ice1
names_hydrometeors_sbmfast['QICED']='Cloud dentrites'

list_hydrometeor_variables_sbmfast.append('QICEP')
colors_hydrometeors_sbmfast['QICEP']=color_ice2
names_hydrometeors_sbmfast['QICEP']='Cloud plates'

list_hydrometeor_variables_sbmfast.append('QSNOW')
colors_hydrometeors_sbmfast['QSNOW']=color_snow
names_hydrometeors_sbmfast['QSNOW']='Snow'

list_hydrometeor_variables_sbmfast.append('QGRAUP')
colors_hydrometeors_sbmfast['QGRAUP']=color_graupel
names_hydrometeors_sbmfast['QGRAUP']='Graupel'

list_hydrometeor_variables_sbmfast.append('QHAIL')
colors_hydrometeors_sbmfast['QHAIL']=color_hail
names_hydrometeors_sbmfast['QHAIL']='Hail'

#RAMS:
list_hydrometeor_variables_rams=[]
colors_hydrometeors_rams={}
names_hydrometeors_rams={}

list_hydrometeor_variables_rams.append('RCP')
colors_hydrometeors_rams['RCP']=color_cloud
names_hydrometeors_rams['RCP']='Cloud droplets'

list_hydrometeor_variables_rams.append('RDP')
colors_hydrometeors_rams['RDP']=color_drizzle
names_hydrometeors_rams['RDP']='Drizzle drops'

list_hydrometeor_variables_rams.append('RRP')
colors_hydrometeors_rams['RRP']=color_rain
names_hydrometeors_rams['RRP']='Rain drops'

list_hydrometeor_variables_rams.append('RPP')
colors_hydrometeors_rams['RPP']=color_ice
names_hydrometeors_rams['RPP']='Pristine ice'

list_hydrometeor_variables_rams.append('RSP')
colors_hydrometeors_rams['RSP']=color_snow
names_hydrometeors_rams['RSP']='Snow'

list_hydrometeor_variables_rams.append('RAP')
colors_hydrometeors_rams['RAP']=color_ice1
names_hydrometeors_rams['RAP']='Aggregates'

list_hydrometeor_variables_rams.append('RGP')
colors_hydrometeors_rams['RGP']=color_graupel
names_hydrometeors_rams['RGP']='Graupel'

list_hydrometeor_variables_rams.append('RHP')
colors_hydrometeors_rams['RHP']=color_hail
names_hydrometeors_rams['RHP']='Hail'

def hydrometeors_colors(microphysics_scheme=None):
    Hydrometeros_colors={}
    Hydrometeors_names={}

    if microphysics_scheme=='morrison':
            Hydrometeros_colors=colors_hydrometeors_morrison
            Hydrometeors_names=names_hydrometeors_morrison

    elif microphysics_scheme=='thompson':
            Hydrometeros_colors=colors_hydrometeors_thompson
            Hydrometeors_names=names_hydrometeors_thompson

    elif microphysics_scheme=='sbmfast':
            Hydrometeros_colors=colors_hydrometeors_sbmfast
            Hydrometeors_names=names_hydrometeors_sbmfast

    elif microphysics_scheme=='sbmfull':
            Hydrometeros_colors=colors_hydrometeors_sbmfull
            Hydrometeors_names=names_hydrometeors_sbmfull

    elif microphysics_scheme=='rams':
            Hydrometeros_colors=colors_hydrometeors_rams
            Hydrometeors_names=names_hydrometeors_rams
            
    else:
        raise ValueError('Unknown microphysics_scheme ' +str(microphysics_scheme) + ', must be morrison, thompson, sbmfast, sbmfull or rams')
    return Hydrometeros_colors,Hydrometeors_names


def water_content_from_hydrometeor(Hydrometeors,microphysics_scheme=None):
    from iris.cube import CubeList
    if microphysics_scheme=='morrison':
            list_liquid_hydrometeors=['QCLOUD','QRAIN']
            list_frozen_hydrometeors=['QICE','QSNOW','QGRAUP']

    elif microphysics_scheme=='thompson':
            list_liquid_hydrometeors=['QCLOUD','QRAIN']
            list_frozen_hydrometeors=['QICE','QSNOW','QGRAUP']

    elif microphysics_scheme=='sbmfast':
            list_liquid_hydrometeors=['QCLOUD','QRAIN']
            list_frozen_hydrometeors=['QICE','QSNOW','QGRAUP']

    elif microphysics_scheme=='sbmfull':
            list_liquid_hydrometeors=['QCLOUD','QRAIN']
            list_frozen_hydrometeors=['QICE','QSNOW','QGRAUP']

    elif microphysics_scheme=='rams':
            list_liquid_hydrometeors=['RCP','RDP','RRP']
            list_frozen_hydrometeors=['RGP','RHP','RAP','RSP','RPP']
    else:
        raise ValueError('Unknown microphysics_scheme ' +str(microphysics_scheme) +', must be morrison, thompson, sbmfast, sbmfull or rams')
    
    liquid_water_content=Hydrometeors.extract_strict(list_liquid_hydrometeors[0])
    if len(list_liquid_hydrometeors)>1:
        for hydrometeor in list_liquid_hydrometeors[1:]:
            liquid_water_content=liquid_water_content+Hydrometeors.extract_strict(hydrometeor)
    liquid_water_content.rename('liquid_water_content')
    
    ice_water_content=Hydrometeors.extract_strict(list_frozen_hydrometeors[0])
    if len(list_liquid_hydrometeors)>1:
        for hydrometeor in list_frozen_hydrometeors[1:]:
            ice_water_content=ice_water_content+Hydrometeors.extract_strict(hydrometeor)
    ice_water_content.rename('ice_water_content')
    
    total_water_content=liquid_water_content+ice_water_content
    total_water_content.rename('total_water_content')

    water_content=CubeList([total_water_content,liquid_water_content,ice_water_content])
    return water_content
