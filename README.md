# CheckMK Things
Some scripts that we have made to make CheckMK more useful to our organization.

## DICOM Echo
This script enables a monitored host (perhaps the CheckMK server itself) to perform DICOM echo tests to endpoints. It depends on Python, the DCM4CHE Toolkit 2.0.15 (and by extension, Java). This script can be added multiple times to support querying multiple DICOM hosts. Once up and running, CheckMK will gather the DICOM status (Critical/OK) as well as the response time.

![image](https://user-images.githubusercontent.com/98006216/206751755-f4840f60-0105-4712-84cf-6a4d488fc23d.png)

#### To Configure:
- Download the DCM4CHE Toolkit 2.0.15 to your server, move it to a safe location (ex **/etc/dcm4che/2.0.15/**)
- Download the files to your server. Move the dicom.py script to a safe location (ex **/opt/scripts/**). Move the dicom_example script to the CheckMK agent's plugins directory (**/usr/lib/check_mk_agent/plugins**).
- Rename the dicom_example script to a name that is meaningful to you (ex dicom_pacs) then open it in an editor. Modify the path to the python script to reflect where you placed it in step 2. Fill in the placeholders with your AE Title, Hostname, and DICOM port.
- Duplicate this script as many times as you need, just make sure each one has a unique name.
- Run a service discovery on the host in CheckMK. If needed, you can troubleshoot the plugin by running **check_mk_agent** at the command line. Assuming your agent has no other custom plugins, the very last few lines should contain the DICOM information being sent to the CheckMK server.
---
## RDS Licenses [(Source)](https://github.com/tribe29/checkmk/blob/master/agents/windows/plugins/rds_licenses.vbs)
This is a fixed version of the rds_licenses.vbs plugin that ships with the windows agent by default. The stock plugin includes built-in/temporary CALs. This script has a modified WQL query to exclude Keypack IDs 4 and 2 (these may or may not be the ones that you need to exclude - check in RD Licensing Manager and adjust the query in the script accordingly).

### What changed:
- Line 56:
  - **Select * from Win32_TSLicenseKeyPack** to **Select * from Win32_TSLicenseKeyPack where KeyPackId !=4 and KeyPackId !=2**
