from collections import defaultdict

import logging

def split_sign_variable(filename,variable,name_neg,name_pos,add_coordinates=None,constraint=None):
    from wrfcube import loadwrfcube
    cube=loadwrfcube(filename,variable,add_coordinates=add_coordinates,constraint=constraint)
    list_out=[]
    list_out.append(get_variable_neg(cube,name_neg))
    list_out.append( get_variable_pos(cube,name_pos))
    return list_out


def split_sign_variable_rams(filename,variable,name_neg,name_pos,add_coordinates=None,constraint=None):
    from ramscube import loadramscube
    cube=loadramscube(filename,variable,add_coordinates=add_coordinates,constraint=constraint)
    list_out=[]
    list_out.append(get_variable_neg(cube,name_neg))
    list_out.append( get_variable_pos(cube,name_pos))
    return list_out

def get_variable_pos(cube,name_neg):
   import numpy as np
   cube_neg=cube[:]
   cube_neg.data=np.clip(cube.data,a_max=np.inf,a_min=0)
   cube_neg.rename(name_neg)
   return cube_neg

def get_variable_neg(cube,name_pos):
   import numpy as np
   cube_pos=cube[:]
   cube_pos.data=np.abs(np.clip(cube.data,a_min=-np.inf,a_max=0))
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
thompson_processes_mass_split['PRR_RCS']=['PRR_RCS','E_PRR_RCS']
thompson_processes_mass_split['PRR_RCG']=['PRR_RCG','E_PRR_RCG']
thompson_processes_mass_split['PRI_IDE']=['PRI_IDE','E_PRI_IDE']
thompson_processes_mass_split['PRS_RCS']=['PRS_RCS','E_PRS_RCS']
thompson_processes_mass_split['PRS_SDE']=['PRS_SDE','E_PRS_SDE']
thompson_processes_mass_split['PRG_GDE']=['PRG_GDE','E_PRG_GDE']
thompson_processes_mass_split['PRG_RCG']=['PRG_RCG','E_PRG_RCG']

List_Processes_Thompson_Mass_signed=list(List_Processes_Thompson_Mass).extend(['E_PRW_VCD,E_PRR_RCS','E_PRR_RCG','E_PRI_IDE','E_PRS_RCS','E_PRS_SDE','E_PRG_GDE','E_PRG_RCG'])


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
morrison_processes_mass_split['PCC']=['EPCC','PCC']
morrison_processes_mass_split['PRCI']=['EPRCI','PRCI']

Proclist_Morr_mass_signed=list(Proclist_Morr_mass).extend(['EPCC','EPRCI'])

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
#Morr_Processes_signed_colors['EPRCI']='blue'
#
#
##
#

#Start setting things up for the SBM:
    
# SBM Full (Dummy variables at the moment)

SBMfull_processes_mass=['P_FRZ_ICE',
                        'P_FRZ_HAIL', 
                        'P_MLT_ICE',
                        'P_MLT_SNOW',
                        'P_MLT_GRAUP',
                        'P_MLT_HAIL']
SBMfull_processes_number=['QVAPOR','QCLOUD']
SBMfull_processes_mass_split=dict()
SBMfull_processes_number_split=dict()




def load_wrf_variables_signed(filename,variable_list,split_dict,add_coordinates=None,constraint=None,quantity='mixing ratio',absolute_value=False,parallel_pool=None,debug_nproc=None,verbose=False):
    from wrfcube import loadwrfcube, derivewrfcube
    from iris.cube import CubeList
    from iris.analysis.maths import abs
    cubelist_out=CubeList()
    
    if (debug_nproc is not None):
        variable_list=variable_list[1:debug_nproc+1]

    List_signed=list(split_dict.keys())


    add_coordinates_load=add_coordinates[:]
    if quantity=='volume':
        rho=derivewrfcube(filename,'density',add_coordinates=add_coordinates,constraint=constraint)
    if 'z' in add_coordinates:   
        cube=loadwrfcube(filename,variable_list[1],add_coordinates=add_coordinates,constraint=constraint)
        z_coord=cube.coord('geopotential_height')
        #p_coord=cube.coord('pressure')
        z_data_dims=cube.coord_dims('geopotential_height')
        add_coordinates_load.remove('z')
    for variable in variable_list:
        if verbose:
            logging('loading'+ str(variable))

        if variable in List_signed:
            List_1=split_sign_variable(filename,variable,split_dict[variable][0],split_dict[variable][1],add_coordinates=add_coordinates_load,constraint=constraint)
            if 'z' in add_coordinates:
                for i,variable in enumerate(List_1):
                   variable.add_aux_coord(z_coord,z_data_dims)
                   List_1[i]=variable
                   #proc.add_aux_coord(p_coord,z_data_dims)
            if quantity=='volume':
                for i,variable in enumerate(List_1):
                    name=variable.name()
                    List_1[i]=(rho*variable)
                    List_1[i].rename(name) 
            cubelist_out.extend(List_1)
        else:
            cube=loadwrfcube(filename,variable,add_coordinates=add_coordinates_load,constraint=constraint)
            #cube.data=np.abs(cube.data)
            cube=abs(cube)
            if 'z' in add_coordinates:
                cube.add_aux_coord(z_coord,z_data_dims)
                #cube.add_aux_coord(p_coord,z_data_dims)
            if quantity=='volume':
                cube=cube*rho
            cube.rename(variable)
            cubelist_out.append(cube)
    return cubelist_out

def load_rams_variables_signed(filename,variable_list,split_dict,
                               add_coordinates=None,constraint=None,
                               quantity='mixing ratio',accumulated=True,
                               dt_out=None,
                               absolute_value=False,
                               parallel_pool=None,
                               debug_nproc=None,verbose=False):
    from ramscube import loadramscube, deriveramscube
    from iris.cube import CubeList
    from iris.analysis.maths import abs
    cubelist_out=CubeList()
    
    if (debug_nproc is not None):
        variable_list=variable_list[1:debug_nproc+1]

    List_signed=list(split_dict.keys())


    add_coordinates_load=add_coordinates[:]
    if quantity=='volume':
        rho=deriveramscube(filename,'density',add_coordinates=add_coordinates,constraint=constraint)
    for variable in variable_list:
        if verbose:
            logging('loading'+ str(variable))

        if variable in List_signed:
            List_1=split_sign_variable(filename,variable,split_dict[variable][0],split_dict[variable][1],
                                       add_coordinates=add_coordinates_load,constraint=constraint)
            if quantity=='volume':
                for i,variable in enumerate(List_1):
                    name=variable.name()
                    List_1[i]=(rho*variable)
                    List_1[i].rename(name) 
            cubelist_out.extend(List_1)
        else:
            cube=loadramscube(filename,variable,add_coordinates=add_coordinates_load,constraint=constraint)
            #cube.data=np.abs(cube.data)
            cube=abs(cube)
            if quantity=='volume':
                cube=cube*rho
            cube.rename(variable)
            cubelist_out.append(cube)
        if not accumulated:
            for cube in cubelist_out:
                cube=cube/dt_out
            
    return cubelist_out


#
#Hydropath_list=[
#    'VAPORCLOUD',
#    'VAPORRAIN',
#    'VAPORICE',
#    'VAPORSNOW',
#    'VAPORGRAUP',
#    'CLOUDRAIN',
#    'CLOUDICE',
#    'CLOUDSNOW',
#    'CLOUDGRAUP',
#    'RAINICE',
#    'RAINSNOW',
#    'RAINGRAUP',
#    'ICESNOW',
#    'ICEGRAUP',
#    'SNOWGRAUP']
#
#def calculate_wrf_morr_path_hydrometeors(filename):
#    Dict={}
#    #Cubelist=[]
#    for path in Hydropath_list:
#        cube=calculate_wrf_morr_path(filename,path)
#        #Cubelist.append(cube)
#        Dict[path]=cube
#    #return Cubelist
#    return Dict
#
#Phasepath_list=['vaporliquid','vaporfrozen','liquidfrozen']
#
#def calculate_wrf_morr_path_phases(filename):
#    Dict={}
#    #Cubelist=[]
#    for path in Phasepath_list:
#        logging('loading '+  path)
#        cube=calculate_wrf_morr_path(filename,path)
#        logging(path + ' loaded')
#
#        #Cubelist.append(cube)
#        Dict[path]=cube
#    #return Cubelist
#    return Dict

#def calculate_wrf_thompson_path(filename,path,add_coordinates=None,quantity='volume'):
#    if (path=='processes_mass'):
#        out=load_wrf_thom_mass_proc(filename,add_coordinates)
#    if (path=='processes_number'):
#        out=load_wrf_thom_number_proc(filename,add_coordinates)
#    else:
#        logging('option not avaliable')
#    return out


thompson_processes_mass= list(List_Processes_Thompson_Mass)
#thompson_processes_mass_split={}
thompson_processes_number= list(List_Processes_Thompson_Number)
thompson_processes_number_split={}

def calculate_wrf_mp_path(filename,processes=None,microphysics_scheme=None, signed=False,constraint=None,add_coordinates=None,quantity='mixing ratio',parallel_pool=None,debug_nproc=None,verbose=False):
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

        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)



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
        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)


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
        cube_list_out=load_wrf_variables_signed(filename,variable_list=process_list,split_dict=split_dict,add_coordinates=add_coordinates,quantity=quantity,constraint=constraint,parallel_pool=parallel_pool,debug_nproc=debug_nproc,verbose=verbose)
 
    
    
    else:
        raise ValueError("Unknown microphysics_scheme")

 
    return cube_list_out


def calculate_RAMS_mp_path(filename,processes=None,microphysics_scheme=None,
                           signed=False,constraint=None,add_coordinates=None,
                           quantity='mixing ratio',accumulated='False',
                           parallel_pool=None,
                           dt_out=None,
                           debug_nproc=None,verbose=False):
    if microphysics_scheme=='morrison':
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

    #for process in Processes:
        #Processes_signed_colors[process.name()]='gray'
  
    #set colors for specific processes: 
    if microphysics_scheme=='morrison':
        
        if colors_processes=='lumped':
            Processes_signed_colors=lumped_colors_morrison
        else:
         
    
    
    
            if colors_processes=='all':
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
    
                Processes_signed_colors['EPRCI']='blue'
                Processes_signed_names['EPRCI']='EPRCI'
                
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
color_melting=        '#ff9a00'   #  orange
color_deposition=     '#34dabe'   #  cyan
color_sublimation=    '#8d5cbf'    #  purple
color_autoconversion= '#90db26'   #  green
color_ice=            '#D4F0FF'   #  icy blue




list_lumped_names_morrison=[]
list_lumped_processes_morrison=[]
lumped_colors_morrison={}

list_lumped_names_morrison.append('Condensation')
list_lumped_processes_morrison.append(['PCC','PCCN'])
lumped_colors_morrison['Condensation']=color_condensation

list_lumped_names_morrison.append('Evaporation')
list_lumped_processes_morrison.append(['EPCC','PRE'])
lumped_colors_morrison['Evaporation']=color_evaporation

list_lumped_names_morrison.append('Freezing')
list_lumped_processes_morrison.append(['MNUCCC','MNUCCR','PSACWS','PSACWI','PIACR','QMULTG','QMULTRG','QMULTS','PRACS','QMULTR','PSACWG','PGRACS','PRACG','PGSACW','QICF','QGRF','QNIRF'])
lumped_colors_morrison['Freezing']=color_freezing

list_lumped_names_morrison.append('Melting')
list_lumped_processes_morrison.append(['PSMLT','PGMLT','PRACI','QIIM'])
lumped_colors_morrison['Melting']=color_melting

list_lumped_names_morrison.append('Rain formation')
list_lumped_processes_morrison.append(['PRC','PRA'])
lumped_colors_morrison['Rain formation']=color_autoconversion

list_lumped_names_morrison.append('Deposition')
list_lumped_processes_morrison.append(['PRD','PRDS','PRDG','MNUCCD'])
lumped_colors_morrison['Deposition']=color_deposition

list_lumped_names_morrison.append('Sublimation')
list_lumped_processes_morrison.append(['EPRD','EPRDS','EPRDG','EVPMS','EVPMG',])
lumped_colors_morrison['Sublimation']=color_sublimation

list_lumped_names_morrison.append('Ice processes')
list_lumped_processes_morrison.append(['PRAI','EPRCI','PRCI','PRACIS','PSACR'])
lumped_colors_morrison['Ice processes']=color_ice

lumped_colors_morrison['Other']='grey'
                
                      
list_lumped_names_thompson=[]
list_lumped_processes_thompson=[]
lumped_colors_thompson={}

list_lumped_names_thompson.append('Condensation')
list_lumped_processes_thompson.append(['E_PRW_VCD'])
lumped_colors_thompson['Condensation']=color_condensation

list_lumped_names_thompson.append('Evaporation')
list_lumped_processes_thompson.append(['PRW_VCD','PRV_REV'])
lumped_colors_thompson['Evaporation']=color_evaporation

list_lumped_names_thompson.append('Freezing')
list_lumped_processes_thompson.append(['PRG_RFZ','PRI_WFZ','PRI_RFZ','PRR_RCG','PRG_GCW','PRG_SCW','PRS_SCW','PRR_RCS','PRG_RCS','PRR_RCI','PRI_WFI'])
lumped_colors_thompson['Freezing']=color_freezing


list_lumped_names_thompson.append('Melting')
list_lumped_processes_thompson.append(['PRR_GML','E_PRR_RCG', 'PRW_IMI']) #missing:'PRR_SML',
lumped_colors_thompson['Melting']=color_melting

list_lumped_names_thompson.append('Rain formation')
list_lumped_processes_thompson.append(['PRR_WAU','PRR_RCW'])
lumped_colors_thompson['Rain formation']=color_autoconversion

list_lumped_names_thompson.append('Deposition')
list_lumped_processes_thompson.append(['E_PRS_SDE','E_PRG_GDE','PRS_IDE','PRI_INU','PRI_IHA'])#,'E_PRI_SDI'??
lumped_colors_thompson['Deposition']=color_deposition

list_lumped_names_thompson.append('Sublimation')
list_lumped_processes_thompson.append(['PRG_GDE','PRS_SDE','PRI_IDE'])
lumped_colors_thompson['Sublimation']=color_sublimation

list_lumped_names_thompson.append('Ice processes')
list_lumped_processes_thompson.append(['PRI_IHA','PRS_SCI','PRS_IAU','PRI_IHM','PRS_IHM','PRG_IHM'])
lumped_colors_thompson['Ice processes']=color_ice


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
list_lumped_processes_sbmfull.append(['P_FRZ_ICE','P_FRZ_HAIL'])
lumped_colors_sbmfull['Freezing']=color_freezing

list_lumped_names_sbmfull.append('Melting')
list_lumped_processes_sbmfull.append(['P_MLT_ICE','P_MLT_SNOW','P_MLT_GRAUP','P_MLT_HAIL'])
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



def lump_cubelist(cubelist_in,list_names_in, list_cubes_in,lumping='all',others=True):
    from iris.cube import CubeList
    if lumping=='all':
        list_names=list_names_in
        list_cubes=list_cubes_in

    if lumping=='latent':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Condensation','Evaporation','Freezing','Melting','Deposition','Sublimation']:
                list_names.append(list_names_in[i])
                list_cubes.append(list_cubes_in[i])

    if lumping=='mass':
        list_names=[]
        list_cubes=[]
        for i,name in enumerate(list_names_in):
            if name in ['Autoconv./Accr.','Ice processes']:
                list_names.append(list_names_in[i])
                list_cubes.append(list_cubes_in[i])


    
    cubelist_out=CubeList()
    list_cubes_other=[cube.name() for cube in cubelist_in]
    for i,name in enumerate(list_names):
        # Summ al cubes in list_cubes[i] and add them to output cubelist:
        #logging(cubelist_in)
        #logging(list_cubes[i])

        cubelist=cubelist_in.extract(list_cubes[i])
        if cubelist:
            cube=sum(cubelist)
            cube.rename(name)        
            cubelist_out.append(cube)
        #Remove these list_cubes from "Other"
        list_cubes_other=list(set(list_cubes_other)-set(list_cubes[i]))
    #Addd allremaining list_cubes and call them "other"
    if others:
        cubelist=cubelist_in.extract(list_cubes_other)
        if cubelist:
            cube=sum(cubelist)
            cube.rename('Other')
            cubelist_out.append(cube)

    return cubelist_out


def lump_processes(processes_in,microphysics=None,lumping='all',others=True):
    if (microphysics=='morrison'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_morrison, list_lumped_processes_morrison,lumping=lumping,others=others)
    elif (microphysics=='thompson'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_thompson, list_lumped_processes_thompson,lumping=lumping,others=others)       
    elif (microphysics=='SBM_full'):
        processes_out=lump_cubelist(processes_in,list_lumped_names_sbmfull, list_lumped_processes_sbmfull,lumping=lumping,others=others)               
    else:
        raise ValueError('microphysics must be morrison, thompson or SBM_full')
    return processes_out


def lumped_latentheating(lumped_processes):
    from iris.cube import CubeList
    from iris.coords import AuxCoord
    cubelist_out=CubeList()
    SLH_fusion = AuxCoord(334e3,long_name='specific latent heat of fusion', units='joules per kilogram')
    SLH_vaporisation = AuxCoord(2.26476e6,long_name='specific latent heat of vaporisation', units='joules per kilogram')
    SLH_fusion_vaporisation = AuxCoord(334e3+2.26476e6,long_name='specific latent heat of fusion and vaporisation', units='joules per kilogram')

    for cube in lumped_processes:
        name=cube.name()
        if (name !='Rain formation' and name !='Ice processes'):
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
    LHRFRZ=lumped_latentheating.extract_strict('Melting')+lumped_latentheating.extract_strict('Freezing').data
    LHRFRZ.rename('LHRFRZ')
    LHREVP=lumped_latentheating.extract_strict('Condensation')+lumped_latentheating.extract_strict('Evaporation').data
    LHREVP.rename('LHREVP')
    LHRSUB=lumped_latentheating.extract_strict('Sublimation')+lumped_latentheating.extract_strict('Deposition').data
    LHRSUB.rename('LHRSUB')
    cubelist_out.extend([LHRFRZ,LHREVP,LHRSUB])
    return cubelist_out

def latentheating_total(lumped_latentheating):
    LHR=lumped_latentheating.extract_strict('Melting')+lumped_latentheating.extract_strict('Freezing').data +lumped_latentheating.extract_strict('Condensation').data+lumped_latentheating.extract_strict('Evaporation').data+lumped_latentheating.extract_strict('Sublimation')+lumped_latentheating.extract_strict('Deposition').data
    LHR.rename('LHR')
    return LHR




    
#def calculate_wrf_morr_path(filename,path,add_coordinates=None,quantity='volume',slice_time=slice(None)):
#    if (path=='processes_mass'):
#        out=load_wrf_morr_mass_proc(filename,add_coordinates,quantity)
#    if (path=='processes_number'):
#        out=load_wrf_morr_num_proc(filename,add_coordinates,quantity)
#    if path=='hydrometeor':
#        out=calculate_wrf_morr_path_hydrometeors(filename)
#    if path=='phase':
#        out=calculate_wrf_morr_path_phases(filename)
#    if (path=='vaporliquid'):
#        out=calculate_wrf_morr_path_vaporliquid(filename)
#    if path=='vaporfrozen':
#        out=calculate_wrf_morr_path_vaporfrozen(filename)
#    if path=='liquidfrozen':
#        out=calculate_wrf_morr_path_liquidfrozen(filename)
#    if path=='VAPORCLOUD':
#        out=calculate_wrf_morr_path_VAPORCLOUD(filename)
#    if path=='VAPORRAIN':
#        out=calculate_wrf_morr_path_VAPORRAIN(filename)
#    if path=='VAPORICE':
#        out=calculate_wrf_morr_path_VAPORICE(filename)
#    if path=='VAPORSNOW':
#        out=calculate_wrf_morr_path_VAPORSNOW(filename)
#    if path=='VAPORGRAUP':
#        out=calculate_wrf_morr_path_VAPORGRAUP(filename)
#    if path=='CLOUDRAIN':
#        out=calculate_wrf_morr_path_CLOUDRAIN(filename)
#    if path=='CLOUDICE':
#        out=calculate_wrf_morr_path_CLOUDICE(filename)
#    if path=='CLOUDSNOW':
#        out=calculate_wrf_morr_path_CLOUDSNOW(filename)
#    if path=='CLOUDGRAUP':
#        out=calculate_wrf_morr_path_CLOUDGRAUP(filename)
#    if path=='RAINICE':
#        out=calculate_wrf_morr_path_RAINICE(filename)
#    if path=='RAINSNOW':
#        out=calculate_wrf_morr_path_RAINSNOW(filename)
#    if path=='RAINGRAUP':
#        out=calculate_wrf_morr_path_RAINGRAUP(filename)
#    if path=='ICESNOW':
#        out=calculate_wrf_morr_path_ICESNOW(filename)
#    if path=='ICEGRAUP':
#        out=calculate_wrf_morr_path_ICEGRAUP(filename)
#    if path=='SNOWGRAUP':
#        out=calculate_wrf_morr_path_SNOWGRAUP(filename)
#    else:
#        logging('path string unknown')
#    return out
#
#def calculate_wrf_morr_latentheating(filename):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    LHREVP=loadwrfcube(filename,'LHREVP')
#    LHRFRZ=loadwrfcube(filename,'LHRFRZ')
#    LHRSUB=loadwrfcube(filename,'LHRSUB')
#    LHR=-1*LHREVP+LHRFRZ+LHRSUB
#    LHR.rename('latent heating rate')
#    return LHR
#
#
#
#def calculate_wrf_morr_path_VAPORCLOUD(filename,slice_time=slice(None)):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates VAPOR/CLOUD')
#    PCC= loadwrfcube(filename, 'PCC3D')
#    #PCCN=loadwrfcube(filename, 'PCCN3D')
#    P_VAPORCLOUD = PCC#+PCCN
#    P_VAPORCLOUD.rename('P_VAPORCLOUD')
#    return P_VAPORCLOUD
#
#def calculate_wrf_morr_path_VAPORRAIN(filename,slice_time=slice(None)):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates VAPOR/RAIN')
#    P_VAPORRAIN = loadwrfcube(filename, 'PRE3D')  #EVAP OF RAIN
#    P_VAPORRAIN.rename('P_VAPORRAIN')
#
#    return P_VAPORRAIN
#
#def calculate_wrf_morr_path_VAPORICE(filename,slice_time=slice(None)):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates VAPOR/ICE')
#    PRD=loadwrfcube(filename, 'PRD3D')     # DEP CLOUD ICE
#    EPRD=loadwrfcube(filename, 'EPRD3D')     # SUBLIMATION CLOUD ICE
#    MNUCCD=loadwrfcube(filename, 'MNUCCD3D') # CHANGE Q FREEZING AEROSOL (PRIM ICE NUCLEATION)
#    P_VAPORICE = PRD + EPRD + MNUCCD
#    P_VAPORICE.rename('P_VAPORICE')
#    return P_VAPORICE
#
#def calculate_wrf_morr_path_VAPORSNOW(filename,slice_time=slice(None)):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates VAPOR/SNOW')
#    EVPMS=loadwrfcube(filename, 'EVPMS3D') # CHANGE Q MELTING SNOW EVAPORATING
#    EPRDS=loadwrfcube(filename, 'EPRDS3D') #    SUBLIMATION SNOW
#    P_VAPORSNOW=EVPMS+EPRDS
#    P_VAPORSNOW.rename('P_VAPORSNOW')
#    return P_VAPORSNOW
#
#def calculate_wrf_morr_path_VAPORGRAUP(filename,slice_time=slice(None)):
#    #Load and add up all process rates between water vapour and cloud droplets
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates VAPOR/GRAUPEL')
#    EVPMG= loadwrfcube(filename, 'EVPMG3D')  # CHANGE Q MELTING OF GRAUPEL AND EVAPORATION
#    PRDG=loadwrfcube(filename,'PRDG3D')  # DEP OF GRAUPEL
#    EPRDG=loadwrfcube(filename, 'EPRDG3D')  #  SUB OF GRAUPEL
#    P_VAPORGRAUPEL=EVPMG+PRDG+EPRDG
#    P_VAPORGRAUPEL.rename('P_VAPORGRAUPEL')
#    return P_VAPORGRAUPEL
#
#def calculate_wrf_morr_path_CLOUDRAIN(filename,slice_time=slice(None)):
#    #Load and add up all process rates between cloud droplets and rain
#    from wrfcube import loadwrfcube
#    #logging('calculate process rates CLOUD/RAIN')
#    PRA= loadwrfcube(filename, 'PRA3D')      # ACCRETION DROPLETS BY RAIN
#    PRC= loadwrfcube(filename, 'PRC3D')    # AUTOCONVERSION DROPLETS
#    P_CLOUDRAIN=PRA+PRC
#    P_CLOUDRAIN.rename('P_CLOUDRAIN')
#    return P_CLOUDRAIN
#
#
#def calculate_wrf_morr_path_CLOUDICE(filename,slice_time=slice(None)):
#    #Load and add up all process rates between ckoud droplets and cloud ice
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates CLOUD/ICE')
#    PSACWI=loadwrfcube(filename, 'PSACWI3D')   # CHANGE Q DROPLET ACCRETION BY CLOUD ICE
#    QMULTS=loadwrfcube(filename, 'QMULTS3D')  # CHANGE Q DUE TO ICE MULT DROPLETS/SNOW
#    QMULTG=loadwrfcube(filename, 'QMULTG3D')   # CHANGE Q DUE TO ICE MULT DROPLETS/GRAUPEL
#    P_CLOUDICE =PSACWI+QMULTS+QMULTG
#    P_CLOUDICE.rename('P_CLOUDICE')
#    return P_CLOUDICE
#
#
#def calculate_wrf_morr_path_CLOUDSNOW(filename,slice_time=slice(None)):
#    #Load and add up all process rates between cloud droplets and snow
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates CLOUD/ICE')
#    PSACWS= loadwrfcube(filename, 'PSACWS3D')      # CHANGE Q DROPLET ACCRETION BY SNOW
#    P_CLOUDSNOW=PSACWS
#    P_CLOUDSNOW.rename('P_CLOUDSNOW')
#    return P_CLOUDSNOW
#
#def calculate_wrf_morr_path_CLOUDGRAUP(filename,slice_time=slice(None)):
#    #Load and add up all process rates between cloud droplets and graupel
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates CLOUD/GRAUP')
#    PSACWG=loadwrfcube(filename, 'PSACWG3D')      #  CHANGE IN Q COLLECTION DROPLETS BY GRAUPEL
#    PGSACW=loadwrfcube(filename, 'PGSACW3D')   # CONVERSION Q TO GRAUPEL DUE TO COLLECTION DROPLETS BY SNOW
#    P_CLOUDGRAUP = PGSACW + PSACWG
#    P_CLOUDGRAUP.rename('P_CLOUDGRAUP')
#    return P_CLOUDGRAUP
#
#
#def calculate_wrf_morr_path_RAINICE(filename,slice_time=slice(None)):
#    #Load and add up all process rates between rain and cloud ice
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates RAIN/ICE')
#    QMULTR=loadwrfcube(filename, 'QMULTR3D')      # CHANGE Q DUE TO ICE RAIN/SNOW
#    QMULTRG=loadwrfcube(filename, 'QMULTRG3D')                         # CHANGE Q DUE TO ICE MULT RAIN/GRAUPEL
#    P_RAINICE = QMULTR+QMULTRG
#    P_RAINICE.rename('P_RAINICE')
#    return P_RAINICE
#
#def calculate_wrf_morr_path_RAINSNOW(filename,slice_time=slice(None)):
#    #Load and add up all process rates between rain and snow
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates RAIN/SNOW')
#    PSMLT=loadwrfcube(filename, 'PSMLT3D')     # CHANGE Q MELTING SNOW TO RAIN
#    PIACRS=loadwrfcube(filename, 'PIACRS3D')                           #CHANGE QR, ICE RAIN COLLISION, ADDED TO SNOW
#    P_RAINSNOW =PSMLT+PIACRS
#    P_RAINSNOW.rename('P_RAINSNOW')
#    return P_RAINSNOW
#
#def calculate_wrf_morr_path_RAINGRAUP(filename,slice_time=slice(None)):
#    #Load and add up all process rates between rain and graupel
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates RAIN/GRAUPEL')
#    MNUCCR=loadwrfcube(filename, 'MNUCCR3D')     # CHANGE Q DUE TO CONTACT FREEZ RAIN
#    PIACR=loadwrfcube(filename, 'PIACR3D')      # CHANGE QR, ICE-RAIN COLLECTION
#    PRACG=loadwrfcube(filename, 'PRACG3D')      #CHANGE IN Q COLLECTION RAIN BY GRAUPEL
#    PGRACS=loadwrfcube(filename, 'PGRACS3D') # CONVERSION Q TO GRAUPEL DUE TO COLLECTION RAIN BY SNOW
#    PGMLT=loadwrfcube(filename, 'PGMLT3D') #  CHANGE Q MELTING OF GRAUPEL
#    P_RAINGRAUP =MNUCCR+PIACR+PRACG+PGRACS+PGMLT
#    P_RAINGRAUP.rename('P_RAINGRAUP')
#    return P_RAINGRAUP
#
#def calculate_wrf_morr_path_ICESNOW(filename,slice_time=slice(None)):
#    #Load and add up all process rates between cloud ice and snow
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates ICE/SNOW')
#    PRAI = loadwrfcube(filename, 'PRAI3D')      # CHANGE Q ACCRETION CLOUD ICE BY SNOW
#    PRCI=loadwrfcube(filename, 'PRCI3D')      # CHANGE Q AUTOCONVERSIN CLOUD ICE TO SNOW
#    PRACIS=loadwrfcube(filename, 'PRACIS3D')     # CHANGE QI, ICE RAIN COLLISION, ADDED TO SNOW
#    P_ICESNOW = PRAI + PRCI + PRACIS
#    P_ICESNOW.rename('P_ICESNOW')
#    return P_ICESNOW
#
#def calculate_wrf_morr_path_ICEGRAUP(filename,slice_time=slice(None)):
#    #Load and add up all process rates between cloud ice and graupel
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates ICE/GRAUPEL')
#    PRACI=loadwrfcube(filename, 'PRACI3D')     # CHANGE QI, ICE-RAIN COLLECTION
#    P_ICEGRAUP = PRACI
#    P_ICEGRAUP .rename('P_ICEGRAUP ')
#    return P_ICEGRAUP
#
#def calculate_wrf_morr_path_SNOWGRAUP(filename,slice_time=slice(None)):
#    #Load and add up all process rates between snow and graupel
#    from wrfcube import loadwrfcube
#    # logging('calculate process rates SNOW/GRAUPEL')
#    P_SNOWGRAUP = 0*loadwrfcube(filename, 'PRACI3D')   # Dummy zeros, since no pathway process found yet
#    P_SNOWGRAUP.rename('P_SNOWGRAUP')
#    return P_SNOWGRAUP
#
#
#def calculate_wrf_morr_path_vaporliquid(filename,slice_time=slice(None)):
#    #Load and add up all process rates between ice phase and water vapour:
#    #logging('calculate processes deposition/sublimation')
#    PVAPORCLOUD=calculate_wrf_morr_path_VAPORCLOUD(filename)
#    PVAPORRAIN=calculate_wrf_morr_path_VAPORRAIN(filename)
#    P_vaporliquid=  PVAPORCLOUD + PVAPORRAIN
#    P_vaporliquid.rename('PVAPORLIQUID')
#    return P_vaporliquid
#
#def calculate_wrf_morr_path_vaporfrozen(filename,slice_time=slice(None)):
#    #Load and add up all process rates between ice phase and water vapour:
#    #logging('calculate processes deposition/sublimation')
#    PVAPORICE=calculate_wrf_morr_path_VAPORICE(filename)
#    PVAPORSNOW=calculate_wrf_morr_path_VAPORSNOW(filename)
#    PVAPORGRAUP=calculate_wrf_morr_path_VAPORGRAUP(filename)
#    P_vaporfrozen=PVAPORICE+PVAPORSNOW+PVAPORGRAUP
#    P_vaporfrozen.rename('PVAPORFROZEN')
#    return P_vaporfrozen
#
#def calculate_wrf_morr_path_liquidfrozen(filename,slice_time=slice(None)):
#    #Load and add up all process rates between frozen and liquid phase
#    #logging('calculate processes freezing/melting')
#    PCLOUDICE=calculate_wrf_morr_path_CLOUDICE(filename)
#    PRAINICE=calculate_wrf_morr_path_RAINICE(filename)
#    PCLOUDSNOW=calculate_wrf_morr_path_CLOUDSNOW(filename)
#    PRAINSNOW=calculate_wrf_morr_path_RAINSNOW(filename)
#    PRAINGRAUP=calculate_wrf_morr_path_RAINGRAUP(filename)
#    PCLOUDGRAUP=calculate_wrf_morr_path_CLOUDGRAUP(filename)
#    P_liquidfrozen=PCLOUDICE+PRAINICE+PCLOUDSNOW+PRAINSNOW+PRAINGRAUP+PCLOUDGRAUP
#    P_liquidfrozen.rename('PLIQUIDFROZEN')
#
#    return P_liquidfrozen
#
#def sum_cubes(filename,name,list_names):
#    from wrfcube import loadwrfcube
#    P_out=loadwrfcube(filename, list_names[0])
#    for name_i in list_names[1:]:
#        P_out=P_out+loadwrfcube(filename, name_i)
#    P_out.rename(name)
#    return P_out
#
#
#
#
#def calculate_wrf_thom_path_VAPORCLOUD(filename):
#    list_names=['']
#    name='P_VAPORCLOUD'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_VAPORRAIN(filename):
#    #Load and add up all process rates between water vapour and cloud droplets
#    list_names=['']
#    name='P_VAPORRAIN'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_VAPORICE(filename):
#    #Load and add up all process rates between water vapour and cloud droplets
#    list_names=['']
#    name='P_VAPORICE'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_VAPORSNOW(filename):
#    list_names=['']
#    name='P_VAPORSNOW'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_VAPORGRAUP(filename):
#    #Load and add up all process rates between water vapour and cloud droplets
#    list_names=['']
#    name='P_VAPORGRAUPEL'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_CLOUDRAIN(filename):
#     #Load and add up all process rates between water vapour and cloud droplets
#    list_names=['']
#    name='P_CLOUDRAIN'
#    return sum_cubes(filename,name,list_names)
#
#
#def calculate_wrf_thom_path_CLOUDICE(filename):
#    #Load and add up all process rates between ckoud droplets and cloud ice
#    list_names=['']
#    name='P_CLOUDICE'
#    return sum_cubes(filename,name,list_names)
#
#
#
#def calculate_wrf_thom_path_CLOUDSNOW(filename):
#    #Load and add up all process rates between cloud droplets and snow
#    list_names=['']
#    name='P_CLOUDSNOW'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_CLOUDGRAUP(filename):
#    #Load and add up all process rates between cloud droplets and graupel
#    list_names=['']
#    name='P_CLOUDGRAUP'
#    return sum_cubes(filename,name,list_names)
#
#
#def calculate_wrf_thom_path_RAINICE(filename):
#    #Load and add up all process rates between rain and cloud ice
#    list_names=['']
#    name='P_RAINICE'
#    return sum_cubes(filename,name,list_names)
#def calculate_wrf_thom_path_RAINSNOW(filename):
#    #Load and add up all process rates between rain and snow
#    list_names=['']
#    name='P_RAINICE'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_RAINGRAUP(filename):
#    #Load and add up all process rates between rain and graupel
#    list_names=['']
#    name='P_RAINGRAUP'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_ICESNOW(filename):
#    #Load and add up all process rates between cloud ice and snow
#    list_names=['']
#    name='P_ICESNOW'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_ICEGRAUP(filename):
#    #Load and add up all process rates between cloud ice and graupel
#    list_names=['']
#    name='P_ICEGRAUP'
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_SNOWGRAUP(filename):
#    #Load and add up all process rates between snow and graupel
#    list_names=['']
#    name='P_SNOWGRAUP'
#    return sum_cubes(filename,name,list_names)
#
#
#def calculate_wrf_thom_path_vaporliquid(filename):
#    #Load and add up all process rates between ice phase and water vapour:
#    #logging('calculate processes deposition/sublimation')
#    PVAPORCLOUD=calculate_wrf_thom_path_VAPORCLOUD(filename)
#    PVAPORRAIN=calculate_wrf_thom_path_VAPORRAIN(filename)
#    name=('PVAPORLIQUID')
#    return sum_cubes(filename,name,list_names)
#
#def calculate_wrf_thom_path_vaporfrozen(filename):
#    #Load and add up all process rates between ice phase and water vapour:
#    #logging('calculate processes deposition/sublimation')
#    PVAPORICE=calculate_wrf_thom_path_VAPORICE(filename)
#    PVAPORSNOW=calculate_wrf_thom_path_VAPORSNOW(filename)
#    PVAPORGRAUP=calculate_wrf_thom_path_VAPORGRAUP(filename)
#    P_vaporfrozen=PVAPORICE+PVAPORSNOW+PVAPORGRAUP
#    P_vaporfrozen.rename('PVAPORFROZEN')
#    return P_vaporfrozen
#
#def calculate_wrf_thom_path_liquidfrozen(filename):
#    #Load and add up all process rates between frozen and liquid phase
#    #logging('calculate processes freezing/melting')
#    PCLOUDICE=calculate_wrf_thom_path_CLOUDICE(filename)
#    PRAINICE=calculate_wrf_thom_path_RAINICE(filename)
#    PCLOUDSNOW=calculate_wrf_thom_path_CLOUDSNOW(filename)
#    PRAINSNOW=calculate_wrf_thom_path_RAINSNOW(filename)
#    PRAINGRAUP=calculate_wrf_thom_path_RAINGRAUP(filename)
#    PCLOUDGRAUP=calculate_wrf_thom_path_CLOUDGRAUP(filename)
#    P_liquidfrozen=PCLOUDICE+PRAINICE+PCLOUDSNOW+PRAINSNOW+PRAINGRAUP+PCLOUDGRAUP
#    P_liquidfrozen.rename('PLIQUIDFROZEN')
#
#    return P_liquidfrozen
#
#

#RAMS microphysics

#RAMS microphysics
RAMS_processes_mass=[
'NUCCLDRT',
'NUCICERT',
'INUCHOMRT',
'INUCCONTR',
'INUCIFNRT',
'INUCHAZRT',
'VAPCLDT',
'VAPRAINT',
'VAPPRIST',
'VAPSNOWT'	,
'VAPAGGRT'	,
'VAPGRAUT',
'VAPHAILT'	,
'VAPDRIZT'	,
'MELTSNOWT',
'MELTAGGRT',
'MELTGRAUT',
'MELTHAILT',
'RIMECLDSNOWT',
'RIMECLDAGGRT',
'RIMECLDGRAUT',
'RIMECLDHAILT',
'RAIN2PRT',
'RAIN2SNT',
'RAIN2AGT',
'RAIN2GRT',
'RAIN2HAT',
'AGGRSELFPRIST',
'AGGRSELFSNOWT',
'AGGRPRISSNOWT'
]


    
# Proclist_Morr_mass=list(morrison_processes_mass)

# morrison_processes_mass_split=defaultdict(dict)
# morrison_processes_mass_split[',PCC']=['EPCC','PCC']
# morrison_processes_mass_split['PRCI']=['EPRCI','PRCI']

# Proclist_Morr_mass_signed=list(Proclist_Morr_mass).extend(['EPCC','EPRCI'])


RAMS_processes_mass_grouped=[
'VAPLIQT',
'VAPICET	',
'MELTICET',
'CLD2RAINT'
'RIMECLDT'
'RAIN2ICET'
'ICE2RAINT'
'AGGREGATET'	
]
    
Proclist_RAMS_mass_grouped=list(morrison_processes_mass)

RAMS_processes_mass_grouped_split=defaultdict(dict)
RAMS_processes_mass_grouped_split['VAPLIQT']=['E_VAPLIQT','VAPLIQT']
RAMS_processes_mass_grouped_split['VAPICET']=['E_VAPICET','VAPICET']

Proclist_Morr_mass_signed=list(Proclist_Morr_mass).extend(['E_VAPLIQT','E_VAPICET'])

list_lumped_names_RAMS=[]
list_lumped_processes_RAMS=[]
lumped_colors_RAMS={}

list_lumped_names_RAMS.append('Condensation')
list_lumped_processes_RAMS.append(['VAPLIQT'])
lumped_colors_RAMS['Condensation']=color_condensation

list_lumped_names_RAMS.append('Evaporation')
list_lumped_processes_RAMS.append(['E_VAPLIQT'])
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