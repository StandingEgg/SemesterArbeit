# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(31.25, 16.25))
    p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=TWO_D_PLANAR, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts['Part-1']
    p.BaseShell(sketch=s)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts['Part-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Material-1')
    mdb.models['Model-1'].materials['Material-1'].Elastic(table=((1000.0, 0.3), ))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-1', 
        material='Material-1', thickness=1.0)
    p = mdb.models['Model-1'].parts['Part-1']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#1 ]', ), )
    region = p.Set(faces=faces, name='Set-1')
    p = mdb.models['Model-1'].parts['Part-1']
    p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Part-1']
    a.Instance(name='Part-1-1', part=p, dependent=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    a = mdb.models['Model-1'].rootAssembly
    s1 = a.instances['Part-1-1'].edges
    side1Edges1 = s1.getSequenceFromMask(mask=('[#1 ]', ), )
    region = a.Surface(side1Edges=side1Edges1, name='Surf-1')
    mdb.models['Model-1'].Pressure(name='Load-1', createStepName='Step-1', 
        region=region, distributionType=UNIFORM, field='', magnitude=100.0, 
        amplitude=UNSET)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['Part-1-1'], )
    a.seedPartInstance(regions=partInstances, size=10.0, deviationFactor=0.1, 
        minSizeFactor=0.1)
    a = mdb.models['Model-1'].rootAssembly
    partInstances =(a.instances['Part-1-1'], )
    a.generateMesh(regions=partInstances)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=174.419, 
        farPlane=224.078, width=140.948, height=64.7497, viewOffsetX=6.91441, 
        viewOffsetY=-0.397238)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=173.802, 
        farPlane=224.695, width=169.097, height=77.6813, viewOffsetX=3.52194, 
        viewOffsetY=-1.3157)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF, datacheckJob=True)
    mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    session.mdbData.summary()
    o3 = session.openOdb(name='E:/Abaqus working directory/Job-1.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o3)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
        'Magnitude'), )
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(
        plotState=CONTOURS_ON_DEF)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), 
        )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), 
        )
    session.viewports['Viewport: 1'].view.setValues(nearPlane=211.279, 
        farPlane=350.73, width=138.171, height=59.6146, viewOffsetX=-1.09484, 
        viewOffsetY=0.570682)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(
        INVARIANT, 'Max. In-Plane Principal'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(
        COMPONENT, 'E11'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(
        COMPONENT, 'E33'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='E', outputPosition=INTEGRATION_POINT, refinement=(
        COMPONENT, 'E12'), )
    session.viewports['Viewport: 1'].view.setValues(nearPlane=212.433, 
        farPlane=349.576, width=138.925, height=59.9402, viewOffsetX=1.24942, 
        viewOffsetY=-3.71693)


