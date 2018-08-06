from collections import defaultdict
from wrfcube import loadwrfcube
import logging

def split_sign_variable(filename,variable,name_neg=None,name_pos=None,add_coordinates=None,constraint=None,absolute_value=False):
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


#Processes_Thompson_Mass_colors={}
#Processes_Thompson_Mass_colors['PRW_VCD']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRV_REV']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRR_WAU']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRR_RCW']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRR_RCS']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRR_RCG']='slategrey'   #  Rain->Graupel
#Processes_Thompson_Mass_colors['PRR_GML']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRR_RCI']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_INU']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_IHM']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_WFZ']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_RFZ']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_IDE']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_RCI']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRI_IHA']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_IAU']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_SCI']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_RCS']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_SCW']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_SDE']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_IHM']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRS_IDE']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_SCW']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_RFZ']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_GDE']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_GCW']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_RCI']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_RCS']='slategrey'   #  Vapor->Water
#Processes_Thompson_Mass_colors['PRG_RCG']='slategrey'   #  Rain->Graupel
#Processes_Thompson_Mass_colors['PRG_IHM']='slategrey'   #  Graupel->Ice

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

#Morr_Processes_signed_colors=defaultdict(dict)
#Morr_Processes_signed_colors['PRD']='lightseagreen'
#Morr_Processes_signed_colors['PRE']='red'
#Morr_Processes_signed_colors['PRDS']='darkorange'
#Morr_Processes_signed_colors['PRA']='darkred'
#Morr_Processes_signed_colors['PRC']='orange'
#Morr_Processes_signed_colors['PCC']='magenta'
#Morr_Processes_signed_colors['PCCN']='blue'
#Morr_Processes_signed_colors['PSMLT']='darkblue'
#Morr_Processes_signed_colors['EVPMS']='azure'
#Morr_Processes_signed_colors['QMULTS']='cyan'
#Morr_Processes_signed_colors['QMULTR']='green'
#Morr_Processes_signed_colors['PRACS']='darkgreen'
#Morr_Processes_signed_colors['PSACWG']='palegreen'
#Morr_Processes_signed_colors['PGSACW']='gray'
#Morr_Processes_signed_colors['PGRACS']='orange'
#Morr_Processes_signed_colors['PRDG']='springgreen'
#Morr_Processes_signed_colors['EPRDG']='coral'
#Morr_Processes_signed_colors['EVPMG']='sage'
#Morr_Processes_signed_colors['PGMLT']='mediumpurple'
#Morr_Processes_signed_colors['PRACI']='lightsteelblue'
#Morr_Processes_signed_colors['PIACRS']='darkslategrey'
#Morr_Processes_signed_colors['PRACIS']='skyblue'
#Morr_Processes_signed_colors['EPRD']='beige'
#Morr_Processes_signed_colors['EPRDS']='saddlebrown'
#Morr_Processes_signed_colors['PRACG']='violet'
#Morr_Processes_signed_colors['QMULTG']='pink'
#Morr_Processes_signed_colors['QMULTRG']='indigo'
#Morr_Processes_signed_colors['MNUCCR']='lightcyan'
#Morr_Processes_signed_colors['MNUCCC']='indigo'
#Morr_Processes_signed_colors['MNUCCD']='indigo'
#Morr_Processes_signed_colors['PRAI']='lime'
#Morr_Processes_signed_colors['PRCI']='peru'
#Morr_Processes_signed_colors['PSACWS']='maroon'
#Morr_Processes_signed_colors['PIACR']='black'
#Morr_Processes_signed_colors['PSACWI']='gold'
#Morr_Processes_signed_colors['PSACR']='lightgray'
#Morr_Processes_signed_colors['EPCC']='lightblue'
#



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




def load_wrf_variables_signed(filename,variable_list,split_dict,add_coordinates=None,constraint=None,quantity='mixing ratio',
                              absolute_value=False,parallel_pool=None,
                              debug_nproc=None,verbose=False):
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
        if verbose:
            logging.debug('loading ' + str(variable))

        if variable in List_signed:
            List_1=split_sign_variable(filename,variable,
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
                          add_coordinates=None,quantity='mixing ratio',parallel_pool=None,debug_nproc=None,verbose=False):
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
                                                constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)

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
                                                debug_nproc=debug_nproc,verbose=verbose)


    elif microphysics_scheme=='SBM_full':
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
                                                constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)
 
    else:
        raise ValueError("Unknown microphysics_scheme")

 
    return cube_list_out


def load_rams_variables_signed(filename,variable_list,split_dict,
                               add_coordinates=None,constraint=None,
                               quantity='mixing ratio',accumulated=True,
                               dt_out=None,
                               absolute_value=False,
                               parallel_pool=None,
                               debug_nproc=None,verbose=False):
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
        if verbose:
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
                           debug_nproc=None,verbose=False):
    if microphysics_scheme=='RAMS':
        if processes=='mass':
            process_list=RAMS_processes_mass_grouped
            #process_list.remove('PCCN')
            if signed==True:
                split_dict=RAMS_processes_mass_grouped_split
            else:
                split_dict={}
        # elif processes=='number':
        #     process_list=morrison_processes_number
        #     if signed==True:
        #         split_dict='morrison_processes_number_split'
        #     else:
        #         split_dict={}    

        cube_list_out=load_rams_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)
 

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

        else:
         
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


    if microphysics_scheme=='thompson':
        
        
        if colors_processes=='lumped':
            Processes_signed_colors=lumped_colors_thompson
            Processes_signed_names=lumped_names_thompson

        else:
            
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

lumped_colors_morrison['Other']='grey'
                
                      
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
list_lumped_processes_thompson.append(['PRR_RCG','PRG_GCW','PRG_SCW','PRS_SCW','PRR_RCS','PRR_RCI'])
lumped_colors_thompson['Riming']=color_riming
lumped_names_thompson['Riming']='Riming'

list_lumped_names_thompson.append('Droplet Riming')
list_lumped_processes_thompson.append(['PRG_GCW','PRG_SCW','PRS_SCW'])
lumped_colors_thompson['Droplet Riming']=color_dropletriming
lumped_names_thompson['Droplet Riming']='Droplet Riming'

list_lumped_names_thompson.append('Rain Riming')
list_lumped_processes_thompson.append(['PRR_RCG','PRR_RCS','PRR_RCI'])
lumped_colors_thompson['Rain Riming']=color_rainriming
lumped_names_thompson['Rain Riming']='Rain Riming'

list_lumped_names_thompson.append('Melting')
list_lumped_processes_thompson.append(['PRR_GML', 'PRW_IMI','PRR_SML','E_PRR_RCG','E_PRR_RCS'])
lumped_colors_thompson['Melting']=color_melting
lumped_names_thompson['Melting']='Melting'

list_lumped_names_thompson.append('Melting to Rain')
list_lumped_processes_thompson.append(['PRR_GML','PRR_SML','E_PRR_RCG','E_PRR_RCS'])
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
#

#list_lumped_names_thompson.append('Sublimation')
#list_lumped_processes_thompson.append(['PRG_GDE','PRS_SDE','PRI_IDE','PRS_IDE'])
#lumped_colors_thompson['Sublimation']=color_sublimation
#lumped_names_thompson['Sublimation']='Sublimation'
#
#list_lumped_names_thompson.append('Graupel Sublimation')
#list_lumped_processes_thompson.append(['PRG_GDE'])
#lumped_colors_thompson['Graupel Sublimation']=color_graupelsublimation
#lumped_names_thompson['Graupel Sublimation']='Graupel Sublimation'
#
#list_lumped_names_thompson.append('Ice Sublimation')
#list_lumped_processes_thompson.append(['PRS_IDE'])
#lumped_colors_thompson['Ice Sublimation']=color_icesublimation
#lumped_names_thompson['Ice Sublimation']='Ice Sublimation'
#
#list_lumped_names_thompson.append('Snow Sublimation')
#list_lumped_processes_thompson.append(['PRS_SDE'])
#lumped_colors_thompson['Snow Sublimation']=color_snowsublimation
#lumped_names_thompson['Snow Sublimation']='Snow Sublimation'
#
#list_lumped_names_thompson.append('Deposition')
#list_lumped_processes_thompson.append(['E_PRI_SDE','E_PRS_SDE','E_PRG_GDE','PRI_INU','PRI_IHA'])
#lumped_colors_thompson['Deposition']=color_deposition
#lumped_names_thompson['Deposition']='Deposition'
#
#list_lumped_names_thompson.append('Graupel Deposition')
#list_lumped_processes_thompson.append(['E_PRG_GDE'])
#lumped_colors_thompson['Graupel Deposition']=color_graupeldeposition
#lumped_names_thompson['Graupel Deposition']='Graupel Deposition'
#
#list_lumped_names_thompson.append('Ice Deposition')
#list_lumped_processes_thompson.append(['E_PRS_SDE','PRI_INU','PRI_IHA'])
#lumped_colors_thompson['Ice Deposition']=color_icedeposition
#lumped_names_thompson['Ice Deposition']='Ice Deposition'
#
#list_lumped_names_thompson.append('Snow Deposition')
#list_lumped_processes_thompson.append(['E_PRI_IDE'])
#lumped_colors_thompson['Snow Deposition']=color_snowdeposition
#lumped_names_thompson['Snow Deposition']='Snow Deposition'

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
#
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
lumped_colors_sbmfull['Other']='grey'


RAMS_processes_mass_grouped=[
'VAPLIQT',
'VAPICET',
'MELTICET',
'CLD2RAINT',
'RIMECLDT',
'RAIN2ICET',
'ICE2RAINT',
'AGGREGATET'	
]
    
Proclist_RAMS_mass_grouped=list(morrison_processes_mass)

RAMS_processes_mass_grouped_split=defaultdict(dict)
RAMS_processes_mass_grouped_split['VAPLIQT']=['E_VAPLIQT','VAPLIQT']
RAMS_processes_mass_grouped_split['VAPICET']=['E_VAPICET','VAPICET']

Proclist_RAMS_mass_signed=list(Proclist_Morr_mass).extend(['E_VAPLIQT','E_VAPICET'])

list_lumped_names_RAMS=[]
list_lumped_processes_RAMS=[]
lumped_colors_RAMS={}

list_lumped_names_RAMS.append('Condensation')
list_lumped_processes_RAMS.append(['E_VAPLIQT'])
lumped_colors_RAMS['Condensation']=color_condensation

list_lumped_names_RAMS.append('Evaporation')
list_lumped_processes_RAMS.append(['VAPLIQT'])
lumped_colors_RAMS['Evaporation']=color_evaporation

list_lumped_names_RAMS.append('Freezing')
list_lumped_processes_RAMS.append(['RIMECLDT','RAIN2ICET'])
lumped_colors_RAMS['Freezing']=color_freezing

list_lumped_names_RAMS.append('Melting')
list_lumped_processes_RAMS.append(['MELTICET'])
lumped_colors_RAMS['Melting']=color_melting

list_lumped_names_RAMS.append('Rain formation')
list_lumped_processes_RAMS.append(['CLD2RAINT'])
lumped_colors_RAMS['Rain formation']=color_autoconversion

list_lumped_names_RAMS.append('Deposition')
list_lumped_processes_RAMS.append(['E_VAPICET'])
lumped_colors_RAMS['Deposition']=color_deposition

list_lumped_names_RAMS.append('Sublimation')
list_lumped_processes_RAMS.append(['VAPICET'])
lumped_colors_RAMS['Sublimation']=color_sublimation

list_lumped_names_RAMS.append('Ice processes')
list_lumped_processes_RAMS.append(['AGGREGATET'])
lumped_colors_RAMS['Ice processes']=color_ice

lumped_colors_RAMS['Other']='grey'



def lump_cubelist(cubelist_in,list_names_in, list_cubes_in,lumping='basic',others=True):
    from iris.cube import CubeList
    if lumping=='basic':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Condensation','Evaporation','Freezing','Melting','Deposition','Sublimation','Rain formation','Ice processes']:
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
    #Add allremaining list_cubes and call them "other"
    if others:
        cubelist=cubelist_in.extract(list_cubes_other)
        if cubelist:
            cube=sum(cubelist)
            cube.rename('Other')
            cubelist_out.append(cube)

    return cubelist_out


def lump_processes(processes_in,microphysics_scheme=None,lumping='basic',others=True):
    if (microphysics_scheme=='morrison'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_morrison, list_lumped_processes_morrison,lumping=lumping,others=others)
    elif (microphysics_scheme=='thompson'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_thompson, list_lumped_processes_thompson,lumping=lumping,others=others)       
    elif (microphysics_scheme=='SBM_full'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_sbmfull, list_lumped_processes_sbmfull,lumping=lumping,others=others)               
    elif (microphysics_scheme=='RAMS'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_RAMS, list_lumped_processes_RAMS,lumping=lumping,others=others)               

    else:
        raise ValueError('microphysics must be morrison, thompson or SBM_full')
    return processes_out


def lumped_latentheating(processes_in,microphysics_scheme=None):
    from iris.cube import CubeList
    from iris.coords import AuxCoord
    cubelist_out=CubeList()
    SLH_fusion = AuxCoord(334e3,long_name='specific latent heat of fusion', units='joules per kilogram')
    SLH_vaporisation = AuxCoord(2.26476e6,long_name='specific latent heat of vaporisation', units='joules per kilogram')
    SLH_fusion_vaporisation = AuxCoord(334e3+2.26476e6,long_name='specific latent heat of fusion and vaporisation', units='joules per kilogram')


    lumped_processes=lump_processes(processes_in,microphysics_scheme=microphysics_scheme,lumping='latent',others=False)
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

def load_latent_heating(filename,microphysics_scheme=None,constraint=None,add_coordinates=None):
    from iris.cube import CubeList
    from wrfcube.wrfcube import variable_list
    
    latent=CubeList()
    
    if 'LHREVP' in variable_list(filename):
            
        LHREVP=loadwrfcube(filename,'LHREVP',constraint=constraint,add_coordinates=add_coordinates)
        LHRFRZ=loadwrfcube(filename,'LHRFRZ',constraint=constraint,add_coordinates=add_coordinates)
        LHRSUB=loadwrfcube(filename,'LHRSUB',constraint=constraint,add_coordinates=add_coordinates)
        

        latent.append(LHREVP)
        latent.append(LHRFRZ)
        latent.append(LHRSUB)
        
        latent.extend(split_sign_variable(filename,'LHREVP',name_neg='latent_heating_rate_of_evaporation',name_pos='latent_heating_rate_of_condensation',add_coordinates=None,constraint=None))
        latent.extend(split_sign_variable(filename,'LHRFRZ',name_neg='latent_heating_rate_of_melting',name_pos='latent_heating_rate_of_freezing',add_coordinates=None,constraint=None))
        latent.extend(split_sign_variable(filename,'LHRSUB',name_neg='latent_heating_rate_of_sublimation',name_pos='latent_heating_rate_of_deposition',add_coordinates=None,constraint=None))

    if microphysics_scheme in ["morrison","thompson"]:
        LHR=LHREVP+LHRFRZ+LHRSUB
        LHR.rename('latent_heating_rate')
        latent.append(LHR)

    elif (microphysics_scheme in ["SBM_full"] and 'LHRTOT' in variable_list(filename)):
        LHR=loadwrfcube(filename,'LHRTOT',constraint=constraint,add_coordinates=add_coordinates)
        LHR.rename('latent_heating_rate')
        latent.append(LHR)

    return latent
