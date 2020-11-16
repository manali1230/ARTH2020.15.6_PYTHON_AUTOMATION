import os
import pyttsx3 as pt
import webbrowser as wp
import time

def AWS():
	flag=0
	os.system('espeak-ng "welcome to AWS Technology" -s 140')
	os.system("clear")
	print("\n\n\n\n\n\n\n")
	tasks=["Configure AWS","Create a Key","Create a Security Group","Launch an Instance","Login Into The Instance","Terminate the Instance","Delete a Security Group","Delete the Key Pair","Create EBS Volume","Attach EBS Volume to EC2 Instance","Delete a Volume","Create S3 Bucket","Upload a Picture on S3","Create CloudFront","Create a Snapshot","Delete The Snapshots","Exit"]
	for i in range(0,len(tasks)):
		print("\t\t\t\t",i+1,". ",tasks[i])
		if i==0:
			os.system("espeak-ng 'press 1 to configure AWS' -s 150")
		elif i==1:
			os.system("espeak-ng 'press 2 to create a key' -s 150")
		elif i==2:
			os.system("espeak-ng 'press 3 to create a Security Group' -s 150")
		elif i==3:
			os.system("espeak-ng 'press 4 to Launch an Instance' -s 150")
		elif i==4:
			os.system("espeak-ng 'press 5 to Login Into The Instance' -s 150")
		elif i==5:
			os.system("espeak-ng 'press 6 to Terminate the Instance' -s 150")
		elif i==6:
			os.system("espeak-ng 'press 7 to Delete a Security Group' -s 150")
		elif i==7:
			os.system("espeak-ng 'press 8 to Delete the Key Pair' -s 150")
		elif i==8:
			os.system("espeak-ng 'press 9 to Create EBS Volume' -s 150")
		elif i==9:
			os.system("espeak-ng 'press 10 to Attach EBS Volume to EC2 Instance' -s 150")
		elif i==10:
			os.system("espeak-ng 'press 11 to Delete a Volume' -s 150")
		elif i==11:
			os.system("espeak-ng 'press 12 to Create S3 Bucket' -s 150")
		elif i==12:
			os.system("espeak-ng 'press 13 to Upload a Picture on S3' -s 150")
		elif i==13:
			os.system("espeak-ng 'press 14 to Create CloudFront' -s 150")
		elif i==14:
			os.system("espeak-ng 'press 15 to Create a Snapshot'")
		elif i==15:
			os.system("espeak-ng 'press 16 to Delete The Snapshot'")
		elif i==16:
			os.system("espeak-ng 'press 17 to Exit'")
	    #espeak-ng("press {} for {}".format(i+1,tasks[i]))
	   
	while True:
		os.system("tput setaf 3")
		if flag==1:
			for i in range(0,len(tasks)):
				print("\t\t\t\t",i+1,". ",tasks[i])
		os.system("espeak-ng 'press a number'")
		n = int(input("press a number : "))
		if n==1:
			os.system("aws configure")
			os.system("espeak-ng 'AWS configured'")
			wp.open("https://ap-south-1.console.aws.amazon.com/console/home?region=ap-south-1")
			flag=1
			time.sleep(5)
		elif n==2:
			os.system("espeak-ng 'Enter Your Key Name'")
			key = input("Enter Your Key Name : ")
			os.system('aws ec2 create-key-pair --key-name {} --query "KeyMaterial" --output text > {}.pem'.format(key,key))
			os.system("espeak-ng 'Your Key is successfully created'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
			flag=1
			time.sleep(10)
		elif n==3:
			os.system("espeak-ng 'Enter Your Security Group Name'")
			sg_name = input("Enter Your Security Group Name: ")
			os.system("espeak-ng 'Enter Your description'")
			description = input("Enter Your description : ")
			os.system("espeak-ng 'Enter Your VPC'")
			vpc_name = input("Enter Your VPC Name : ")
			os.system("espeak-ng 'Enter Your Inbound rule protocol'")
			protocol = input("Enter Your Inbound Rule Protocol : ")
			os.system("espeak-ng 'Enter Your port'")
			port = input("Enter Your Port : ")
			os.system("espeak-ng 'Enter Your CIDR'")
			cidr = input("Enter Your CIDR : ")
			os.system('aws ec2 create-security-group --group-name {} --description "{}" --vpc-id {}'.format(sg_name,description,vpc_name))
			os.system("aws ec2 authorize-security-group-ingress --group-name {}  --protocol {} --port {} --cidr {}".format(sg_name,protocol,port,cidr))
			os.system("espeak-ng 'Your Security Group is successfully created'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
			flag=1
			time.sleep(10)
		elif n==4:
			os.system("espeak-ng 'Enter Your Amazon Machine Image ID'")
			ami = input("Enter Your AMI ID: ")
			os.system("espeak-ng 'Enter the number of instance you want to launch'")
			count = int(input("Enter the number of instance you want to launch : "))
			os.system("espeak-ng 'Enter Your Instance Type'")
			instance_type = input("Enter Your instance type : ")
			os.system("espeak-ng 'Enter Your Key Name'")
			key = input("Enter Your Key Name : ")
			os.system("espeak-ng 'Enter Your Security Group ID'")
			sg_id = input("Enter Your Security Group ID : ")
			os.system("espeak-ng 'Enter Your Subnet ID'")
			subnet_id = input("Enter Your Subnet ID : ")
			os.system('aws ec2 run-instances --image-id {} --count {} --instance-type {} --key-name {} --security-group-ids {} --subnet-id {}'.format(ami,count,instance_type,key,sg_id,subnet_id))
			os.system("espeak-ng 'Your instance is succesfuuly launched'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
			flag=1
			time.sleep(10)
		elif n==5:
			os.system("espeak-ng 'Enter Your user name'")
			username = input("Enter Your User Name : ")
			os.system("espeak-ng 'Enter Your Key name'")
			key = input("Enter Your Key Name : ")
			os.system("espeak-ng 'Enter Your Instance IP'")
			instance_ip = input("Enter Your Instance IP: ")
			os.system("espeak-ng 'Welcome to Your Instance'")
			os.system("ssh -l {} -i {}.pem {}".format(username,key,instance_ip))
			flag=1
			time.sleep(3)
		elif n==6:
			os.system("espeak-ng 'Enter Your instance ID'")
			instance_id = input("Enter Your Instance ID : ")
			os.system("aws ec2 terminate-instances --instance-ids {}".format(instance_id))
			os.system("espeak-ng 'Your instance is succesfully Terminated'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
			flag=1
			time.sleep(10)
		elif n==7:
			os.system("espeak-ng 'Enter Your Security Group name'")
			sg_name = input("Enter Your Security Group name : ")
			os.system("aws ec2 delete-security-group --group-name {}".format(sg_name))
			os.system("espeak-ng 'Your Security Group is successfully deleted'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
			flag=1
			time.sleep(10)
		elif n==8:
			os.system("espeak-ng 'Enter Your Key Name'")
			key = input("Enter Your Key Name : ")
			os.system("aws ec2 delete-key-pair --key-name {}".format(key))
			os.system("rm {}.pem".format(key))
			os.system("espeak-ng 'Your Key is successfully Deleted'")
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
			flag=1
			time.sleep(10)
		elif n==9:
			os.system("espeak-ng 'Enter Your Availability Zone'")
			az = input("Enter Your Availability Zone : ")
			os.system("espeak-ng 'Enter Your Volume Type'")
			volume_type = input("Enter Your Volume Type : ")
			os.system("espeak-ng 'Enter Your Size'")
			size = input("Enter Your Size : ")
			os.system("aws ec2 create-volume --availability-zone {}  --volume-type {}  --size {}".format(az,volume_type,size))
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
			time.sleep(10)
			flag=1
		elif n==10:
			os.system("espeak-ng 'Enter Your Volume ID'")
			volume_id = input("Enter Your Volume ID : ")
			os.system("espeak-ng 'Enter Your Instance ID'")
			instance_id = input("Enter Your Instance ID : ")
			os.system("espeak-ng 'Enter Your Device'")
			device = input("Enter Your Device : ")
			os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(volume_id,instance_id,device))
			#aws ec2 attach-volume --volume-id vol-0509b3cb61afb5f42 --instance-id i-071d7b410c0f5a9d6 --device /dev/sdf
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
			flag=1
			os.system("espeak-ng 'Your Volume is succesfully Attached'")
			time.sleep(10)
		elif n==11:
			os.system("espeak-ng 'Enter Your Volume ID'")
			volume_id = input("Enter Your Volume ID : ")
			os.system("aws ec2 detach-volume --volume-id {}".format(volume_id))
			time.sleep(5)
			os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:")
			flag=1
			os.system("espeak-ng 'Your Volume is succesfully Deleted'")
			time.sleep(10)
		elif n==12:
			os.system("espeak-ng 'Enter Your Unique Bucket Name'")
			bucket = input("Enter Your Unique Bucket Name : ")
			os.system("espeak-ng 'Enter Your Region'")
			region = input("Enter Your Unique Region : ")
			os.system("espeak-ng 'Enter Your Location Constraint'")
			location_constraint = input("Enter Your Unique Location Constraint : ")
			os.system("aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}".format(bucket,region,location_constraint))
			# aws s3api create-bucket --bucket manalibucket --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
			wp.open("https://s3.console.aws.amazon.com/s3/home?region=ap-south-1#")
			flag=1
			os.system("espeak-ng 'Your Bucket is succesfully created'")
			time.sleep(10)
		elif n==13:
			os.system("espeak-ng 'Enter Your Unique Bucket Name'")
			bucket = input("Enter Your Unique Bucket Name : ")
			os.system("espeak-ng 'Enter Your Key'")
			key = input("Enter Your Unique Key : ")
			os.system("aws s3 sync '/root/AWS' s3://{}".format(bucket))
			os.system("aws s3api put-object-acl --bucket {} --key {} --acl public-read".format(bucket,key))
			flag=1
			time.sleep(10)
		elif n==14:
			os.system("espeak-ng 'Enter Your Unique Bucket Name'")
			bucket = input("Enter Your Unique Bucket Name : ")
			os.system("espeak-ng 'Enter Your Default root object'")
			root_object = input("Enter Your Default root object : ")
			os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucket,root_object))
			wp.open("https://console.aws.amazon.com/cloudfront/home?region=ap-south-1#")
			flag=1
			os.system("espeak-ng 'Your CloudFront is succesfully created'")
			time.sleep(10)
		elif n==15:
			os.system("espeak-ng 'Enter Your Volume ID'")
			volume_id = input("Enter Your Volume ID : ")
			os.system("espeak-ng 'Enter Your Description'")
			description = input("Enter Your Description : ")
			os.system('aws ec2 create-snapshot --volume-id {} --description "{}"'.format(volume_id,description))
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Snapshots:sort=snapshotId")
			flag=1
			os.system("espeak-ng 'Your snapshot is succesfully created'")
			time.sleep(10)
		elif n==16:
			os.system("espeak-ng 'Enter Your Snapshot ID'")
			snapshot_id = input("Enter Your Snapshot ID : ")
			os.system('aws ec2 delete-snapshot --snapshot-id {}'.format(snapshot_id))
			wp.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Snapshots:sort=snapshotId")
			flag=1
			os.system("espeak-ng 'Your snapshot is succesfully Deleted'")
			time.sleep(10)
		elif n==17:
			os.system("espeak-ng 'Thank You See You Soon'")
			os.system("clear")
			print("\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tSAYONARA\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			flag=0
			time.sleep(4)
			break
		else:
			os.system("tput setaf 1")
			os.system("espeak-ng 'Enter Correct number'")

def Docker():
	while True:
		os.system("clear")
		os.system("tput setaf 6")
		print("\t\tMenu Program in Python:-")
		print("\t1. Docker Start")
		print("\t2. Docker Run")
		print("\t3. Run Python code on Docker")
		print("\t4. Run Web Server on Docker")
		print("\t5. Remove Docker image")
		print("\t6. See all images")
		print("\t7. Show all running container ")
		print("\t8. Show all container")
		print("\t9. Docker Stop")
		print("\t0. Exit")
		os.system("tput setaf 3")
		choice=int(input("Enter your choice: "))
		if choice==1:
			os.system("systemctl start docker")
			os.system("tput setaf 4")
			print("Docker Started")
		elif choice==2:
			print("Available docker images")
			print("1. centos:latest")
			print("2. centos:7 ")
			print("3. ubuntu")
			img=input("Enter the image name: ")
			name=input("Enter the container name: ")
			os.system("docker run -dit --name {} {}".format(name,img))
			os.system("tput setaf 4")
			print("Container successfully launched")
		elif choice==3:
			print("List of Available containers:- ")
			os.system("docker ps -a")
			name=input("Enter the name of container on which you wish to setup Python Interpreter: ")
			os.system("docker start {}".format(name))
			os.system("docker exec {} yum install python3 -y".format(name))
			os.system("docker exec {} python3".format(name))
			os.system("tput setaf 4")
			print("Python Interpreter Successfully setup on {} container".format(name))
		elif choice==4:
			print("List of Available containers:- ")
			os.system("docker ps -a")
			name=input("Enter the name of container on which you wish to configure web server:- ")
			os.system("docker start {}".format(name))
			os.system("docker exec {}  yum install httpd -y".format(name))
			os.system("docker exec {}  /usr/sbin/httpd ".format(name))
			os.system("tput setaf 4")
			print("Web server successfully configured on {} container".format(name))
		elif choice==5:
			os.system("docker ps -a")
			name=input("Enter the name of the container to remove: ")
			os.system("docker stop {}".format(name))	
			os.system("docker rm  {}".format(name))
			os.system("tput setaf 4")
			print("Container {} successfully removed".format(name))
		elif choice==6:
			os.system("tput setaf 4")
			print("The docker images in this system are:-")
			os.system("docker images ")
		elif choice==7:
			os.system("tput setaf 4")
			print("The currently running containers on this system are:-")
			os.system("docker ps")
		elif choice==8:
			os.system("tput setaf 4")
			print("These are containers present on this system:- ")
			os.system("docker ps -a")
		elif choice==9:
			os.system("systemctl stop docker")
			os.system("tput setaf 4")
			print("Docker Stopped")
		elif choice==0:
			print("Thank You")
			break
		else:
			print("Invalid Choice! Try Again")
		os.system("sleep 5")	

def Linux():
	def avaldisk():
		os.system('tput setaf 6')
		os.system('fdisk -l | less')
		os.system('tput setaf 7')

	def avalpv():
		os.system('tput setaf 6')
		os.system('pvdisplay | less')
		os.system('tput setaf 7')

	def avalvg():
		os.system('tput setaf 6')
		os.system('vgdisplay | less')
		os.system('tput setaf 7')
	def avallv():
		os.system('tput setaf 6')
		os.system('lvdisplay | less')
		os.system('tput setaf 7')

	def pv():
		os.system('clear')
		os.system('tput setaf 1')
		print()
		print("PHYSICAL VOLUME CREATION ")
		print("--------------------------")
		print()
		os.system('tput setaf 3')
		name=input("Enter Hard Disk Name : ")
		x=sp.getstatusoutput('pvcreate {}'.format(name))
		if x[0]== 0 :
		  print('\t\t\t\t\tPHYSICAL VOLUME CREATED')
		  y=sp.getstatus('pvdispaly {}'.format(name))
		  print(y[1])
		else:
		  print("PROCESS FAIL")
		os.system('tput setaf 4')
		z=input("press enter to continue")
		os.system('tput setaf 7')
		





	def vg():
		os.system('clear')
		os.system('')
		print()
		print("VOLUME GROUP CREATION")
		print("\t\t\t----------------")
		print()
		os.system('tput setaf 3')
		name1=input("Enter Group Volume Name : ")
		name2=input("Enter 1 st volume :")
		name3=input("Enter 2nd volume : ")
		x=sp.getstatusoutput('vgcreate {0} {1} {2}'.format(name,name1,name2))
		if x[0]== 0 :
		  print('\t\t\t\t\t VOLUME GROUP CREATED')
		  y=sp.getstatus('vgdispaly {}'.format(name))
		  print(y[1])
		else:
		  print("PROCESS FAIL")		
		os.system('tput setaf 4')
		print(ch)
	def menu():
		while True:
			os.system('clear')
			os.system('tput setaf 1')
			print("                            LVM AUTOMATION WITH PYTHON ")
			print("                            ===========================")
			print()
			os.system('tput setaf 2')
			print("        1.Display All Attached Hard Disk")
			print("        2.Display All Phsical volume")
			print("        3.Display All Volume Group")
			print("        4.Display All Logical Volumes")
			print("        5.Create Physical Volume")
			print("        6.create Volume Group")
			print("        7.create Logical Volume")
			print("        8.Exit")
			print()
			os.system('tput setaf 3')

			ch=input("Enter ur choice : ")
			os.system('tput setaf 6')
			print()
			if int(ch)== 1:
				avaldisk()
				
			elif int(ch)== 2:
				avalpv()
			elif int(ch)== 3:
				avalvg()
			elif int(ch)== 4:
				avallv()
			elif int(ch)== 5:
				pv()
			elif int(ch)== 6:
				vg()
			elif int(ch)== 7:
				lv()
			
			elif int(ch)== 8:
				exit()
			else:
				os.system('tput setaf 7')
				print("wrong command")


	menu()


def Hadoop():
	import os

	os.system("tput setaf 3")
	print("\t\t\t welcome to my hadoop!")
	os.system("tput setaf 7")
	print("\t\t\t.....")
	print("""
		\n
		press1:to know hadoop storage list
		press2:to start the hadoop cluster
		press3:to know how me datenodes connected
		press4:to enter the safemode
		press5:to leave the safemode
		press6:to stop the cluster
		""")
	ch=input("enter your choice from above:")
	print(ch)
	if int(ch)==1:
	    os.system("hadoop fs -ls/")
	elif int(ch)==2:
	    os.system("hadoop-daemon.sh start namenode")
	elif int(ch)==3:
	    os.system("hadoop dfsadmin -report")
	elif int(ch)==4:
	    os.system("hadoop dfsadmin -safemode get")
	elif int(ch)==5:
	    os.system("hadoop dfsadmin -safemode leave")
	elif int(ch)==6:
	    os.system("hadoop-daemon.sh stop namenode")
	else:
	   print( "error")


os.system("tput setaf 3")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\t\t\t\t\tWELCOME\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

os.system('espeak-ng "welcome i am grafitti i am especially programmed to perform AWS , Docker ,Linux , Hadoop task" -s 140')

Technology = ["AWS","Docker","Linux","Hadoop","Exit"]
os.system("tput setaf 4")
for j in range(0,5):
	print("\t\t\t\t",j+1,". ",Technology[j])
	if j==0:
		os.system("espeak-ng 'press 1 For AWS' -s 150")
	elif j==1:
		os.system("espeak-ng 'press 2 for Docker' -s 150")
	elif j==2:
		os.system("espeak-ng 'press 3 for Linux' -s 150")
	elif j==3:
		os.system("espeak-ng 'press 4 for Hadoop' -s 150")
	else:
		os.system("espeak-ng 'press 5 to exit'")

while True:
	os.system("tput setaf 6")
	os.system("espeak-ng 'Enter Your Technology' -s 150")
	select_tech=int(input("Enter Your Technology : "))
	if select_tech == 1:
		AWS()
	elif select_tech == 2:
		Docker()
	elif select_tech == 3:
		Linux()
	elif select_tech == 4:
		Hadoop()
	else:
		break
	

