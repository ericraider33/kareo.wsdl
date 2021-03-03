#!/usr/bin/env python3
# Refernces: 
# https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package-using-the-dotnet-cli
# https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet?tabs=netcore21
#
# To release nuget:
# - From IDE:
#       - Update kareo.wsdl NuGet properties version
#       - Update kareo.wsdl Assembly version
# - build.py nuget
# - Using web, upload result on page: https://www.nuget.org/packages/manage/upload
#
import subprocess, argparse, os, zipfile, shutil, glob, re, platform, pathlib, sys

def minPython(tuple):
    if sys.version_info < tuple:
        sys.exit("Python %s.%s or later is required.\n" % tuple)
minPython((3,7))

parser = argparse.ArgumentParser(description='Builds kareo.wsdl')
parser.add_argument('target', help='Target of either: nuget')

args = parser.parse_args()

def resetDirectory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    if os.path.exists(path) == False:
        os.mkdir(path)
    print("Verified Dependency: resetDirectory=" + path)

def verifyDependencyDotNet():
    subprocess.run(['dotnet','--info'], check=True, capture_output=True)
    print("Verified Dependency: DotNet")    
           
def buildNuget():
    verifyDependencyDotNet()    
    resetDirectory('kareo.wsdl/.out')
       
    # Cleans build
#    print("\n\nRunning Step: Clean")
#    subprocess.run(['dotnet','clean','--configuration','Release'], check=True)

    print("\n\nRunning Step: Restore")
    subprocess.run(['dotnet','restore','kareo.wsdl/kareo.wsdl.csproj'], check=True)
	
    # Pack build
    print("\n\nRunning Step: Pack")
    subprocess.run(['dotnet','pack','--output','.out/lib','kareo.wsdl/kareo.wsdl.csproj'], check=True)
    
    # Prints nuget URL
    print("\nUpload 'nupkg' file to URL: https://www.nuget.org/packages/manage/upload")


##########################
## Runs build
#########################  
    
# Downloads package from build server
if args.target == 'nuget':
    buildNuget()
else:
    raise Exception('Unknown target ' + args.target)
    
print("SUCCESS: build '{0}' complete".format(args.target))






