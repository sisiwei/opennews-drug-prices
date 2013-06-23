# HTML to JSON and CSV for geocoding

import json

# get a HTML page listing pharamacies, city by city
# go to https://apps.health.ny.gov/pdpw/Pharmacy/SearchPharmacy.action
# enter 'New York' or other city for 'City'
# View Source does not work -- use Network or other view to capture HTML

htmlcopy = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/2002/REC-xhtml1-20020801/DTD/xhtml1-strict.dtd">
<html>
	<head>
	<title>Pharmacy Search Results - Prescription Drug Prices in New York State </title>
	<meta name="description" content="New York State Prescription Drug Prices" />
	<meta name="keywords" content="drug, prescription, medication, price, new york" />
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />		
		
				<style type="text/css" media="print"><!--@import url(https://www.health.ny.gov/style/aught5/print.css);--></style>
				
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/banner.css);--></style>
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/navigation.css);--></style>
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/main.css);--></style>
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/homepage.css);--></style>
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/footer.css);--></style>
				
			
			
			
			
			
				<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/safari_konqueror_fixes.css);--></style>
			
			
			<style type="text/css" media="screen"><!--@import url(/pdpw/style/generic.css);--></style>
			<style type="text/css" media="screen"><!--@import url(https://www.health.ny.gov/style/aught5/classes.css);--></style>
			<style type="text/css" media="screen"> <!--@import url(/pdpw/style/webcast.css);--></style>
			<style type="text/css" media="screen"> <!--@import url(/pdpw/style/main.css);--></style>
			<style type="text/css" media="screen"><!--@import url(/pdpw/style/map.css);--></style>
			
		
	</head>
	<body>
		<div id="banner">
	<a href="#skiptocontent" id="skipnav">skip to main content</a>
	<div id="bannercontainerone">
		<div id="bannercontainertwo">
			<a href="http://www.ny.gov/"><img src="https://health.ny.gov/images/state_banner/new_york_state_169x28.png" id="nys_image" alt="NY.gov Portal" /></a>
			<a href="http://www.nysegov.com/citGuide.cfm?superCat=102&amp;cat=449&amp;content=main"><img src="https://health.ny.gov/images/state_banner/state_agencies_134x28png.png" id="state_agency_image" alt="State Agency Listing" /></a>
	 
			<!-- search graphic -->
	 		<a href="#" onclick="document.getElementById('sw_searchbox').style.display= 'block'; document.getElementById('searchgraphic').style.display= 'none';document.getElementById('searchbox').focus();"><img id="searchgraphic" src="https://health.ny.gov/images/state_banner/search_140x28.png" alt="Search all of NY.gov" /></a>
	 
	 
			<!--state wide search box-->
			<form style="float:right;" id="sw_searchbox" action="http://www.search.cio.ny.gov/search" method="get" >
			<p>
	       		<input value="date:D:L:d1" name="sort" type="hidden" />
			<input value="xml_no_dtd" name="output" type="hidden" />
			<input value="UTF-8" name="ie" type="hidden" />
			<input value="UTF-8" name="oe" type="hidden" />
	 
			<input value="default_frontend" name="client" type="hidden" />
		  	<input value="default_frontend" name="proxystylesheet" type="hidden"/>
		  	<input value="default_collection" name="site" type="hidden" />
	 
			<label for="NYSsearchbox" style="color:#003063;">Search all of NY.gov</label>
			<input type="text" size="20" name="q" maxlength="256" id="NYSsearchbox" title="Search" />
			<input type="submit" id="NYSsearchbutton" value="Search NY.GOV" />
	 
			</p>
			</form>
	 
			<script type="text/javascript">
			 // If JavaScript is on, manipulate search control objects.
			 // Otherwise this will be ignored and search controls will be shown by default
				 document.getElementById('sw_searchbox').style.display = 'none';
	 			 document.getElementById('searchgraphic').style.display= 'block';
			 </script>
			


		</div>
	</div>
	
	<h2 id="doh"><a href="https://www.health.ny.gov/" title="Return to DOH home page">Department of Health</a></h2>
	<div id="global">
			<div id="healthy">Information for a Healthy New York</div>
			<ul>
				<li><a href="https://www.health.ny.gov/"><span>Home</span></a></li>
				<li><a href="https://www.health.ny.gov/contact/"><span>Contact</span></a></li>
				<li><a href="https://www.health.ny.gov/help/"><span>Help</span></a></li>
				<li><a href="https://www.health.ny.gov/es/index.htm" lang="es"><span>En Espa&ntilde;ol</span></a></li>
				<li><a href="https://www.health.ny.gov/healthaz/"><span>A-Z Index</span></a></li>
			</ul>
	</div>
</div>
				
	
		<div id="torso">
			
<div id="mainnavigation" >
	<h2> About This Site </h2>
	<ul>
		<li><a href="/pdpw/SearchDrugs/Home.action" title="Search Drug Prices" > Search Drug Prices</a></li> 
		<li><a href="/pdpw/Pharmacy/SearchPharmacy.action" title="Search for Pharmacies" > Search for Pharmacies</a></li>
		<li><a href="/pdpw/ConsumerInfo.action" title="Consumer Information">Consumer Information</a></li>
		<li><a href="/pdpw/Faq.action" title="Frequently Asked Questions"> Frequently Asked Questions </a></li>
		<li><a href="/pdpw/Contact.action" title="Contact Us"> Contact Us</a></li>
	</ul>
</div>
			
<div id="main">
	<div id="breadcrumbs">You are Here: <a href="https://www.health.ny.gov/">Home Page</a> 
		<strong>&gt;</strong> <a href="/pdpw/SearchDrugs/Home.action">  Prescription Drug Price Website </a>
		<strong>&gt;</strong> <a href="/pdpw/Pharmacy/SearchPharmacy.action"> Search for Pharmacies </a>
		<strong>&gt;</strong> Pharmacy Search Results
	</div>  

				
<form id="SearchByCity" name="SearchByCity" onsubmit="return true;" action="/pdpw/Pharmacy/SearchByCity.action" method="post">
	<input type="hidden" name="struts.token.name" value="struts.token" />
<input type="hidden" name="struts.token" value="6LHZ7NEGXBM69K018OZD236D0YVW28N7" />
	<div id="content">
	<a name="skiptocontent"></a>
		<h1 class="site_title"> Prescription Drug Prices in New York State </h1>
		<h2 class="page_title_small"> Search Results for Pharmacies in New York State  </h2>	
	
		<div>
		  <a id="SearchByCity_" href="/pdpw/Pharmacy/SearchPharmacy.action" title="Start Over">
		  	<img src="../images/startover.png" alt="Start Over" />
		  </a>
		</div>

		
		
		
		
		
		
			<table >
			
			
			<tr>
				<th scope="row" align="left">City  </th>
				<td> New York  </td>
			</tr>
			
			
			
			
			
			
			<tr>
				<th scope="row" align="left"> Number of Pharmacies  </th>
				<td>  682 </td>
			</tr>
			</table>

			
			
			
			
			
			
			<table width="75%">
				<tr>
					<td>
						<table  width="100%" >
						<tr><td align="right"> 
							<img src="../images/printicon.gif" alt="Printable Version" /> 
								
									<a id="SearchByCity_" href="/pdpw/Pharmacy/PrintSearchByCity.action" title="Printable version">
										 Printable Version
									</a>
															
								
								
				 			</td>
				 		</tr>
						</table>
					</td>
				</tr>
				<tr>
					<td>
						<table class="webcasttable" width="100%" >
							<tr>
								<th align="left"> Pharmacy  </th>
								
								
								
								<th align="left"> Price List </th>
								<th align="left"> Map </th>
							</tr>			
	
																			
							<tr class="">
								<td> 
								    
									10 PARK PHARMACY, INC.<br/>
									53 E. 34TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 683-3838
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19404"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19404&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19404"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19404&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									124 RX CORP.<br/>
									157 WEST 124TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 865-0295
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28767"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28767&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28767"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28767&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									133RD STREET PHARMACY INC.<br/>
									1473 AMSTERDAM AVE<br/>
									
										STORE 1<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 491-4911
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27564"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27564&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27564"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27564&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									139 PHARMACY INC.<br/>
									3415 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 283-6623
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15978"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15978&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15978"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15978&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									1491 LEX PHARMACY INC.<br/>
									1491 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 289-3665
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27656"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27656&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27656"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27656&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									158 RX CORP.<br/>
									11 EDWARD MORGAN PLACE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 234-1800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29684"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29684&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29684"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29684&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									1699 FANCY PHARMACY INC.<br/>
									131 ESSEX ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 529-4532
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19989"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19989&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19989"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19989&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									1721 CARNEGIE HILL PHARMACY INC.<br/>
									1721 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31604"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31604&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31604"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31604&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									181 PHARMACY INC.<br/>
									565 W. 181 ST. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 543-2616
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25953"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25953&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25953"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25953&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									1875 LEXINGTON AVENUE CORP. OF NEW YORK<br/>
									C/O PHARMACY<br/>
									
										1875 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 410-0911
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28368"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28368&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28368"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28368&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									2000 NINOS INC.<br/>
									3663 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 491-2910
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31805"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31805&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31805"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31805&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									2000 NINOS PHARMACY INC.<br/>
									3663 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 491-2910
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22880"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22880&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22880"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22880&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									2355 2ND AVE CORP.<br/>
									2355 2ND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 426-7151
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28194"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28194&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28194"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28194&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									255 COLUMBUS AVENUE CORPORATION<br/>
									255 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 362-9170
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15922"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15922&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15922"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15922&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									27 AUDUBON PHARMACY CORP.<br/>
									27 AUDUBON AVE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(646) 448-4848
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29811"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29811&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29811"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29811&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									27 BROADWAY DRUGS INC.<br/>
									2721 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 866-6700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19014"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19014&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19014"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19014&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									3 W 137 PHARMACY &amp; MEDICAL SUPPLY  INC.<br/>
									3 WEST 137 STREET<br/>
									
										STORE 2<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 281-4881
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28317"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28317&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28317"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28317&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									3-9 DRUGS, INC.<br/>
									102 NAGLE AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 942-5050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17397"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17397&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17397"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17397&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									311 PHARMACY CORP.<br/>
									522 WEST 181ST STREET<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 740-3737
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26599"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26599&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26599"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26599&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									3340 BROADWAY PHARMACY #2 INC.<br/>
									3621 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 926-9800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27032"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27032&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27032"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27032&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									3340 BROADWAY PHARMACY, INC.<br/>
									3340 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 281-1270
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22629"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22629&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22629"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22629&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									370 PHARMACY CORP.<br/>
									370 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 684-8700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28883"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28883&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28883"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28883&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									3817 BROADWAY PHARMACY INC.<br/>
									3835 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 927-0220
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21013"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21013&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21013"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21013&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									3890 BROADWAY PHARMACY IV, INC<br/>
									3898 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 568-0975
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27458"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27458&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27458"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27458&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									420 2ND AVE DRUG CORP.<br/>
									331 E. 23RD. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 683-0148
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22924"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22924&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22924"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22924&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									58TH STREET PHARMACY, INC.<br/>
									428 WEST 59TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 333-7330
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20261"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20261&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20261"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20261&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									66 NAGLE AVENUE CORP.<br/>
									66 NAGLE AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 304-3949
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22529"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22529&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22529"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22529&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									731 PHARMACY CORP.<br/>
									691 COLUMBUS AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 222-4400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21082"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21082&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21082"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21082&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									79TH STREET PHARMACY, INC.<br/>
									215 WEST 79TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31405"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31405&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31405"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31405&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									82 COLUMBUS CORP.<br/>
									463 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 721-3883
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20292"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20292&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20292"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20292&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									88TH STREET DRUG CORP.<br/>
									1695 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 348-8900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26359"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26359&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26359"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26359&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									909 COLUMBUS RX CORP.<br/>
									909 COLUMBUS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 222-6388
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29000"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29000&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29000"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29000&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									92 PHARMACY INC.<br/>
									1938 SECOND AVENUE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 426-6484
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25557"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25557&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25557"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25557&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									A. GOLDBERGER'S PRESCRIPTIONS SINCE 1898 INC.<br/>
									1200 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 734-6998
									
								</td>
								
								

								<td> <a  name="PriceLink" id="13108"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=13108&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="13108"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=13108&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									A.M. PHARMACY II INC.<br/>
									219 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 226-8832
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30883"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30883&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30883"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30883&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									A.P.K.G. PHARMACY INC.<br/>
									360 E. 4TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 677-7335
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18167"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18167&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18167"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18167&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ABA NOUB, LTD.<br/>
									216 WEST 72ND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 875-1718
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21409"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21409&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21409"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21409&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ABACUS PHARMACY INC.<br/>
									168 2ND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 477-6400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31022"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31022&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31022"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31022&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ABC PHARMACY V CORP.<br/>
									26 E. BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 965-8882
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30509"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30509&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30509"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30509&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AHORRE DRUG CORP.<br/>
									746 10TH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 581-6010
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16867"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16867&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16867"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16867&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AID PHARMACY (NY), CORP.<br/>
									139 CENTRE STREET<br/>
									
										STORE #108<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 965-9688
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28867"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28867&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28867"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28867&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AJANTA PHARMACY INC.<br/>
									2718 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10030	<br/>														
									
									  Phone:&nbsp;(212) 283-6228
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18218"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18218&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18218"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18218&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AKSHAR HEALTH CORP.<br/>
									165 W. 127TH STREET<br/>
									
										UNIT 10<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 222-2340
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26168"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26168&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26168"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26168&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ALISONS PHARMACY, INC.<br/>
									12 BOWERY STREET.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 227-7065
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22271"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22271&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22271"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22271&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ALL HEALTH PHARMACY CORP.<br/>
									118 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 431-4398
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25350"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25350&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25350"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25350&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ALLEN STREET PHARMACY INC.<br/>
									2 ALLEN STREET<br/>
									
										SUITE 1C/1D<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 966-8287
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31800"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31800&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31800"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31800&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AMAR PHARMACY INC.<br/>
									4446 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 567-6151
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18237"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18237&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18237"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18237&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AMI PHARMACY, INC.<br/>
									4180 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 923-5733
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22847"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22847&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22847"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22847&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ANDY PHARMACY INC.<br/>
									3750 BROADWAY, STORE #4<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 368-5511
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26550"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26550&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26550"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26550&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									APPLE DRUG INC.<br/>
									1207 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 758-9614
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18307"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18307&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18307"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18307&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ARROW PHARMACY INC.<br/>
									883 NINTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 245-8469
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3384"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3384&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3384"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3384&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ASTA SURGICAL-CHEMIST INC.<br/>
									108-13 JAMAICA AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;11418	<br/>														
									
									  Phone:&nbsp;(718) 847-5997
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23723"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23723&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23723"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23723&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AUDUBON PHARMACY INC.<br/>
									85 AUDUBON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 543-2937
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26548"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26548&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26548"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26548&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AVALON CHEMISTS INC.<br/>
									7 SECOND AVE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 260-3131
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28107"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28107&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28107"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28107&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AVALON PHARMACY INC.<br/>
									7 SECOND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 260-3131
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29728"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29728&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29728"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29728&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AVENUE A PHARMACY INC.<br/>
									41 AVENUE A<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 260-4878
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26385"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26385&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26385"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26385&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									AVIGNONE CHEMISTS, LTD<br/>
									281 SIXTH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 242-3033
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27398"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27398&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27398"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27398&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									AVN PHARMACY INC.<br/>
									2240 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 534-1937
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22343"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22343&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22343"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22343&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									B. EIDINGER AND SON DRUG CORPORATION<br/>
									250 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 475-1144
									
								</td>
								
								

								<td> <a  name="PriceLink" id="6599"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=6599&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="6599"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=6599&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									B.N.D. PHARMACY INC.<br/>
									277 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 228-2260
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22154"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22154&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22154"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22154&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BARMED DRUGS INC.<br/>
									1394 YORK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 249-1777
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17546"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17546&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17546"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17546&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BATTERY PARK PHARMACY INC.<br/>
									327 SOUTH END AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10280	<br/>														
									
									  Phone:&nbsp;(212) 912-0555
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17898"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17898&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17898"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17898&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BAYARD L.C. PHARMACY CORPORATION<br/>
									62 BAYARD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-8116
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22079"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22079&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22079"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22079&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BBRX1 LLC<br/>
									207 EAST 66TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 717-7797
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26501"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26501&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26501"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26501&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BBRX2 LLC<br/>
									523 HUDSON STREET<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 741-7111
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27671"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27671&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27671"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27671&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BEEKMAN PHARMACY, INC.<br/>
									19 BEEKMAN STREET<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 766-1942
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29459"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29459&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29459"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29459&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BELLEPLAINE PHARMACY INC.<br/>
									2703 FREDERICK DOUGLAS<br/>
									
										BLVD.<br/>
									
									
									NEW YORK,NY&nbsp;10030	<br/>														
									
									  Phone:&nbsp;(212) 234-0300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31665"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31665&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31665"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31665&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BEST CARE PHARMACY CORP.<br/>
									28 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 334-0086
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20781"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20781&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20781"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20781&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BEST PHARMACY INC.<br/>
									2002 SECOND AVE.<br/>
									
										STORE 1<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 410-4410
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30807"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30807&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30807"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30807&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BIOMED DRUGS AND SURGICAL SUPPLY CO. INC.<br/>
									C/O PHARMACY<br/>
									
										50 3RD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 388-0340
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22379"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22379&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22379"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22379&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BIOSCRIP PHARMACY, INC.<br/>
									197 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 691-9050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25005"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25005&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25005"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25005&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BIRAJ PHARMACY CORP.<br/>
									1280 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 928-8082
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22143"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22143&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22143"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22143&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BLISS PHARMACY INC.<br/>
									1590 MADISON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 427-4382
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18424"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18424&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18424"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18424&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BOAN DRUGS INC.<br/>
									1873 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 690-1331
									
								</td>
								
								

								<td> <a  name="PriceLink" id="14562"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=14562&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="14562"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=14562&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BOWEN PHARMACY, INC.<br/>
									881 TENTH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 956-9111
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29176"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29176&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29176"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29176&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BOWERY PHARMACY, INC.<br/>
									95 BOWERY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 219-0449
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18560"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18560&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18560"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18560&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BPB DRUGS, INC.<br/>
									131 EAST 60TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 838-6765
									
								</td>
								
								

								<td> <a  name="PriceLink" id="9990"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=9990&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="9990"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=9990&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BRENTWOOD PHARMACY LLC<br/>
									48 WEST 8TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30375"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30375&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30375"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30375&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BRISELY PHARMACY, INC.<br/>
									4229 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 781-6314
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18799"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18799&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18799"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18799&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BROADWAY DOWNTOWN PHARMACY, INC.<br/>
									373 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 925-4888
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22384"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22384&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22384"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22384&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BROADWAY PHARMACY III, INC<br/>
									629 WEST 185TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 927-0999
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27346"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27346&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27346"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27346&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BROADWAY PHARMACY NYC, INC<br/>
									4740 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 942-1234
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29616"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29616&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29616"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29616&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									BUENA VISTA PHARMACY INC.<br/>
									2022 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 369-4018
									
								</td>
								
								

								<td> <a  name="PriceLink" id="12457"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=12457&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="12457"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=12457&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									BUY-RITE CORP.<br/>
									185 CANAL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 925-7698
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21143"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21143&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21143"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21143&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									C &amp; C DRUG, INC.<br/>
									1-7 AUDUBON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 543-1554
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25051"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25051&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25051"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25051&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									C.O. BIGELOW CHEMISTS, INC.<br/>
									414 6TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 533-2700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3435"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3435&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3435"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3435&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CALIGOR RX INC.<br/>
									1226 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 369-6000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25078"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25078&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25078"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25078&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CAMBRIDGE CHEMISTS INC.<br/>
									855 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 734-5678
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3484"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3484&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3484"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3484&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CANAL PHARMACY INC.<br/>
									196 CANAL STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 608-1668
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27630"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27630&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27630"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27630&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CANAL STREET PHARMACY INC.<br/>
									210-212 CANAL STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 748-4900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28411"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28411&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28411"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28411&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CANALBERRY CORP.<br/>
									84 MULBERRY STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 619-6190
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26925"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26925&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26925"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26925&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CAPITOL CHEMISTS INC.<br/>
									1639 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 879-1258
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3491"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3491&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3491"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3491&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CARE WELL PHARMACY,INC.<br/>
									1868 THIRD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 369-1350
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25433"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25433&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25433"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25433&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CARNEGIE HILL CHEMISTS, INC.<br/>
									1842 2ND AVE<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 987-5494
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29812"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29812&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29812"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29812&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CARNEGIE HILL PHARMACY, INC.<br/>
									1331 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 534-1300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29534"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29534&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29534"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29534&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CENTRAL PARK WEST ALACHEMISTS, INC.<br/>
									25 CENTRAL PARK WEST<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 247-8080
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28255"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28255&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28255"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28255&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CENTRAL PHARMACY CORP.<br/>
									138 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-0750
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18497"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18497&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18497"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18497&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CENTRE STREET PHARMACEUTICAL LLC.<br/>
									139 CENTRE ST.<br/>
									
										RETAIL #4<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 343-1919
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30024"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30024&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30024"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30024&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CENTURY GRAND, INC.<br/>
									302A GRAND ST<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 925-3838
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30556"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30556&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30556"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30556&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CHARMAR INC.<br/>
									2253 3RD AVE.<br/>
									
										3RD FLOOR<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-1821
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19085"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19085&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19085"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19085&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CHELSEA PHARMACY INC<br/>
									165 WEST 20TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 255-9900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31488"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31488&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31488"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31488&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CHELSEA ROYAL CARE PHARMACY, INC.<br/>
									154 NINTH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 255-8000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30272"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30272&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30272"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30272&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CHINATOWN PHARMACY CORP.<br/>
									111 MOTT STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31073"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31073&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31073"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31073&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CHOI &amp; TAM INC.<br/>
									106-110 LAFAYETE ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 966-9239
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24994"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24994&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24994"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24994&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CHRISTOPHER A. BASSOLINO PHARMACY CORP.<br/>
									1260 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 289-9168
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20550"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20550&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20550"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20550&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CIARLETTA, ANTHONY P. &amp; BUCICH, CARLO<br/>
									LATO-ASCIONE PHARMACY<br/>
									
										2268 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-0811
									
								</td>
								
								

								<td> <a  name="PriceLink" id="13443"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=13443&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="13443"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=13443&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CIPA PHARMACY INC.<br/>
									1000 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 753-8638
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23207"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23207&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23207"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23207&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CITY DRUGS NY CORP.<br/>
									1273 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 988-4500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30951"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30951&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30951"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30951&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CITYDRUG &amp; SURGICAL, INC.<br/>
									2039 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 781-1011
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22649"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22649&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22649"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22649&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CLAYTON &amp; EDWARD CHEMISTS, INC<br/>
									1004 LEXINGTON AVE<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 737-1147
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27677"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27677&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27677"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27677&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CLEARFIELD COLUMBIA ST. DRUG CORPORATION<br/>
									55 COLUMBIA ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 533-8120
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16250"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16250&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16250"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16250&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CLYDE CHEMISTS, LTD.<br/>
									926 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 744-5050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23498"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23498&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23498"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23498&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CM &amp; P PHARMACY, INC.<br/>
									1600 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 927-5994
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21281"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21281&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21281"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21281&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									COLUMBUS &amp; 103RD ST. DRUG CORP.<br/>
									916 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 663-7440
									
								</td>
								
								

								<td> <a  name="PriceLink" id="13409"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=13409&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="13409"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=13409&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									COMFORT CARE PHARMACY, INC.<br/>
									1990 LEXINGTON AVE<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 410-4200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29849"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29849&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29849"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29849&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									COMMUNICARE, INC.<br/>
									C/O PHARMACY<br/>
									
										30 E. 40TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 684-5125
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28755"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28755&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28755"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28755&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CONFUCIUS PHARMACY INC.<br/>
									139 CENTRE ST.<br/>
									
										STORE #105<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 775-8160
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31606"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31606&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31606"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31606&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CONFUCIUS PHARMACY INC.<br/>
									25 BOWERY ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 966-4420
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16069"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16069&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16069"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16069&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CORAL PHARMACY INC<br/>
									4126 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 795-3894
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27845"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27845&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27845"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27845&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CORBY PHARMA INC.<br/>
									988 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 755-6632
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30135"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30135&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30135"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30135&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CORDETTE DRUG CORP.<br/>
									55 WEST 39TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 398-9999
									
								</td>
								
								

								<td> <a  name="PriceLink" id="9440"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=9440&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="9440"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=9440&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									COSTCO WHOLESALE CORPORATION<br/>
									517 EAST 117TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 896-5882
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29843"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29843&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29843"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29843&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CT HEALTH CASTLE CORP.<br/>
									86 BOWERY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 966-6039
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29977"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29977&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29977"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29977&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CUREWELL DRUGS INC.<br/>
									4157 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 568-1020
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29124"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29124&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29124"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29124&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C<br/>
									C/O PHARMACY<br/>
									
										129 FULTON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 233-5021
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24794"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24794&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24794"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24794&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C<br/>
									222 EAST 34TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 532-2354
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29751"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29751&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29751"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29751&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C<br/>
									C/O PHARMACY<br/>
									
										215 PARK AVENUE SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(646) 602-8237
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24609"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24609&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24609"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24609&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									800 10TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31936"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31936&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31936"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31936&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										320 FIFTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 279-2856
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24247"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24247&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24247"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24247&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1622 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 876-7016
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23235"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23235&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23235"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23235&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1396 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 249-5699
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23337"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23337&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23337"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23337&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										200 WEST END AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 496-4198
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29404"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29404&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29404"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29404&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									81 EIGHTH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30566"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30566&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30566"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30566&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHAMRACY<br/>
									
										338 EAST 23RD STREET<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 505-1555
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23810"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23810&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23810"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23810&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1223 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 752-7703
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24435"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24435&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24435"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24435&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										540 AMSTERDAM AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 712-2821
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24516"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24516&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24516"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24516&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1500 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 289-3846
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26200"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26200&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26200"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26200&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										500 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 677-1008
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24978"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24978&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24978"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24978&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									20 UNIVERSITY PL.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 260-3052
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29670"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29670&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29670"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29670&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									1241 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 535-3438
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29710"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29710&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29710"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29710&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1294 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 996-3000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24499"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24499&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24499"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24499&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										272 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 255-2592
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22461"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22461&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22461"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22461&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										743 AMSTERDAM AVE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 280-0596
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24179"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24179&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24179"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24179&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										630 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(917) 369-8688
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25249"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25249&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25249"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25249&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										75 CHRISTOPHER STREET<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 627-2662
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23809"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23809&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23809"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23809&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										130 DYCKMAN ST.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 304-4698
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24800"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24800&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24800"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24800&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										750 AVENUE OF THE<br/>
									
									
										AMERICAS<br/>
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(646) 336-8388
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24941"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24941&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24941"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24941&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/0 PHARMACY<br/>
									
										115 W. 125TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 864-5431
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25489"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25489&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25489"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25489&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										500 W. 42ND. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 244-4285
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26198"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26198&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26198"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26198&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										130 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 348-2199
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25164"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25164&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25164"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25164&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										253 FIRST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 254-1454
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24264"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24264&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24264"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24264&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										307 SIXTH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 255-5054
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24263"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24263&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24263"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24263&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										1569-1575 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 249-5198
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24455"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24455&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24455"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24455&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									2495 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 787-2194
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29691"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29691&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29691"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29691&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										275 THIRD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 677-4677
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24262"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24262&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24262"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24262&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										158 BLEECKER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 982-3133
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22793"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22793&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22793"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22793&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									C/O PHARMACY #2168<br/>
									
										1 COLUMBUS PL.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 245-0636
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23510"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23510&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23510"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23510&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									300 PARK AVENUE SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 982-5193
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30940"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30940&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30940"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30940&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									CVS ALBANY, L.L.C.<br/>
									500 WEST 23RD ST<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31491"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31491&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31491"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31491&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									CVS ALBANY, LLC.<br/>
									C/O PHARMACY<br/>
									
										150 EAST 42ND ST<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 661-8139
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28610"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28610&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28610"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28610&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DALIZA PHARMACY INC.<br/>
									3481 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 281-9410
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17113"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17113&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17113"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17113&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DBN DRUGS INC.<br/>
									1265 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 781-4214
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25095"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25095&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25095"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25095&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DIN PHARMACY CORP.<br/>
									2015 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 928-4528
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18520"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18520&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18520"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18520&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DJ DRUGS &amp; SURGICALS INC.<br/>
									2381 FREDERICK DOUGLAS<br/>
									
										BLVD.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 749-6626
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31926"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31926&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31926"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31926&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DORVIT PHARMACY INC.<br/>
									1025 A 3RD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 750-4100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29729"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29729&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29729"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29729&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DOWNTOWN PHARMACY, INC.<br/>
									DOWNTOWN PHARMACY<br/>
									
										165 WILLIAM ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 233-0333
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25527"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25527&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25527"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25527&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DRUG SHOPPE LLC<br/>
									2074 8TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26336"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26336&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26336"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26336&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DTH PHARMACY, INC.<br/>
									19 BEEKMAN STREET<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 587-5252
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28047"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28047&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28047"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28047&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										254 PARK AVE SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 533-7580
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18607"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18607&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18607"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18607&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										37 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10006	<br/>														
									
									  Phone:&nbsp;(212) 425-8460
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18608"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18608&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18608"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18608&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1370 6TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 586-2740
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25482"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25482&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25482"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25482&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										17 BATTERY PL. SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10004	<br/>														
									
									  Phone:&nbsp;(212) 248-3922
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25394"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25394&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25394"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25394&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										10 UNION SQUARE EAST<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(646) 602-2491
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28673"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28673&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28673"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28673&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2409 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 874-0238
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26680"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26680&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26680"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26680&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1675 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 348-7400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25376"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25376&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25376"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25376&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										900 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 582-3463
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26950"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26950&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26950"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26950&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										194 EAST 2ND. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 375-9000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25949"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25949&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25949"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25949&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1091 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 794-7100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25115"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25115&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25115"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25115&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										609-B COLUMBUS AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 724-4270
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24185"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24185&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24185"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24185&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2148 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(917) 441-1756
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26592"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26592&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26592"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26592&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										161 EAST 23RD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 477-1372
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23517"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23517&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23517"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23517&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										358-362 5TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 279-0208
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18630"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18630&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18630"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18630&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2307 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 501-8355
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22353"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22353&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22353"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22353&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										50 BOWERY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 608-0301
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25098"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25098&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25098"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25098&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										67 BROAD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10004	<br/>														
									
									  Phone:&nbsp;(212) 943-3690
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18610"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18610&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18610"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18610&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										535 5TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 687-8641
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18613"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18613&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18613"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18613&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										140 WEST 23RD. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 255-5900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25120"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25120&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25120"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25120&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										71 WEST 23RD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 463-8873
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22978"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22978&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22978"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22978&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										585 2ND. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 685-0784
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23786"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23786&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23786"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23786&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1481 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 988-2115
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26803"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26803&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26803"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26803&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										125-133 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 529-7140
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24842"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24842&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24842"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24842&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										300 WEST 135TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10030	<br/>														
									
									  Phone:&nbsp;(212) 491-6015
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27495"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27495&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27495"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27495&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										465 2ND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 326-9030
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23793"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23793&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23793"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23793&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										245 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 388-0800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26961"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26961&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26961"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26961&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										22 W. 48TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 730-4914
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22494"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22494&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22494"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22494&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										280 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10007	<br/>														
									
									  Phone:&nbsp;(212) 233-2742
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25138"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25138&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25138"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25138&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1231 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 360-6586
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23692"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23692&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23692"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23692&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2025 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 579-9955
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24283"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24283&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24283"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24283&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										51 WEST 51ST STREET<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 582-8525
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18620"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18620&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18620"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18620&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										485 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 682-5338
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18623"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18623&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18623"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18623&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										459 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 291-2658
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29144"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29144&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29144"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29144&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									100 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10005	<br/>														
									
									  Phone:&nbsp;(917) 502-9843
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31315"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31315&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31315"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31315&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									BASEMENT<br/>
									
										24 EAST 14TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 337-7650
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26614"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26614&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26614"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26614&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2589 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 864-5246
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24521"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24521&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24521"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24521&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										4 TIMES SQUARE<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(646) 366-8047
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25179"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25179&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25179"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25179&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1627 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 586-0374
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18790"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18790&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18790"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18790&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										4 COLUMBUS CIRCLE<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 265-2302
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25457"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25457&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25457"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25457&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										700 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 864-4189
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23755"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23755&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23755"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23755&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										100 WEST 57TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 956-0464
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20939"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20939&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20939"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20939&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										460 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 244-4026
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20981"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20981&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20981"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20981&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										4 PARK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 683-5532
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20144"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20144&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20144"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20144&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									144 BLEEKER STREET<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(917) 534-1370
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27768"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27768&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27768"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27768&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										775 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 280-3085
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25336"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25336&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25336"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25336&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									771 8TH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 974-6013
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28257"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28257&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28257"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28257&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										55 E. 55TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 750-9095
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19590"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19590&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19590"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19590&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										380 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 579-7246
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23387"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23387&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23387"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23387&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										200 WATER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 385-9353
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23535"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23535&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23535"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23535&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										352 GREENWICH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 406-3700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28834"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28834&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28834"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28834&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										49 E. 52ND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 888-2323
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19499"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19499&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19499"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19499&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										325 COLUMBUS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 580-2017
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29093"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29093&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29093"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29093&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										40 WALL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10005	<br/>														
									
									  Phone:&nbsp;(212) 742-8454
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18631"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18631&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18631"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18631&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1430 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 768-0201
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18625"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18625&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18625"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18625&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1356 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 722-0014
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28826"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28826&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28826"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28826&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1111 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 838-0195
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30722"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30722&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30722"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30722&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										761 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(646) 602-8274
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24390"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24390&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24390"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24390&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										378 6TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 674-5357
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22587"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22587&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22587"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22587&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1270 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 560-9811
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24980"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24980&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24980"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24980&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										196 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 598-0339
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23267"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23267&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23267"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23267&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										180 WEST 20TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 243-0129
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25328"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25328&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25328"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25328&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1191 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 355-5944
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22144"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22144&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22144"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22144&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										ONE PENN PLAZA EAST<br/>
									
									
										CONCOURSE LEVEL<br/>
									
									NEW YORK,NY&nbsp;10119	<br/>														
									
									  Phone:&nbsp;(212) 268-3999
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24803"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24803&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24803"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24803&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										4 WEST 4TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 473-1027
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24717"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24717&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24717"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24717&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										125 EAST 86TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 996-5261
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25553"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25553&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25553"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25553&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2683 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 865-5360
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23746"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23746&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23746"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23746&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									619 9TH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 581-0602
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28514"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28514&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28514"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28514&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										625 8TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 273-0889
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24181"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24181&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24181"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24181&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										399 E. 72ND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 535-9816
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24404"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24404&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24404"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24404&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										155 E. 34TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 683-3042
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23531"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23531&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23531"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23531&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										100 DELANCY ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 253-0270
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23628"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23628&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23628"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23628&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2069 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 799-1067
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30557"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30557&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30557"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30557&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									300 EAST 23RD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(347) 273-2215
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31524"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31524&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31524"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31524&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									315 W 23RD ST<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(646) 486-7430
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27961"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27961&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27961"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27961&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										866 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 759-9412
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22383"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22383&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22383"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22383&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										598 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 343-2567
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21830"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21830&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21830"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21830&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										976-980 AMSTERDAM AVE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 866-4232
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24405"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24405&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24405"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24405&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										425 PARK AVE<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 223-7037
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27514"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27514&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27514"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27514&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										PENN STATION<br/>
									
									
										MAIN CONCOURSE/AMTRAK LVL<br/>
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 760-8107
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22435"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22435&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22435"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22435&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										322 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 255-5025
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23629"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23629&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23629"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23629&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1251 AVE. OF THE AMERICAS<br/>
									
									
									NEW YORK,NY&nbsp;10020	<br/>														
									
									  Phone:&nbsp;(212) 391-1105
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25114"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25114&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25114"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25114&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1052 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(646) 282-0530
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26593"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26593&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26593"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26593&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1150 AVENUE OF AMERICAS<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 221-3588
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18627"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18627&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18627"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18627&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										253 WEST 72ND. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 580-0497
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24979"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24979&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24979"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24979&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1498 YORK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 879-8990
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24472"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24472&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24472"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24472&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									131 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 206-0059
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29946"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29946&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29946"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29946&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										80 MAIDEN LN.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 509-8890
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20298"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20298&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20298"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20298&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1915 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(917) 492-1038
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25540"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25540&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25540"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25540&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										873 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(917) 534-1351
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25288"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25288&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25288"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25288&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2760-62 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 678-7893
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24318"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24318&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24318"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24318&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										250 W. 57TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10107	<br/>														
									
									  Phone:&nbsp;(212) 265-2101
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27769"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27769&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27769"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27769&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										666 3RD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 599-4351
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22297"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22297&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22297"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22297&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										931 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 421-1046
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26749"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26749&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26749"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26749&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										230 PARK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10169	<br/>														
									
									  Phone:&nbsp;(212) 682-1364
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25246"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25246&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25246"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25246&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										777 6TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(646) 336-8414
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24939"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24939&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24939"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24939&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										405 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 808-4743
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21814"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21814&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21814"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21814&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1327 YORK AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 737-6240
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26935"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26935&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26935"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26935&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										135 EAST 125TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(917) 492-3550
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24703"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24703&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24703"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24703&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										401 EAST 86TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(917) 492-8801
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24652"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24652&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24652"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24652&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1279 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 744-2668
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22240"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22240&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22240"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22240&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										188-192 DYCKMAN STREET<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 567-1282
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24880"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24880&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24880"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24880&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										95 WALL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10005	<br/>														
									
									  Phone:&nbsp;(212) 363-5830
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19376"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19376&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19376"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19376&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										773 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 829-0651
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24722"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24722&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24722"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24722&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1646 2ND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 427-6940
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23437"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23437&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23437"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23437&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2864 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 316-5113
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24418"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24418&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24418"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24418&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										630 3RD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 682-3191
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24824"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24824&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24824"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24824&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1 WHITEHALL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 509-9020
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20354"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20354&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20354"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20354&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										260 MADISON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 448-0025
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18626"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18626&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18626"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18626&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										525 7TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 221-8627
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18616"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18616&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18616"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18616&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										585 HUDSON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 541-9708
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18622"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18622&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18622"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18622&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									17 JOHN ST<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 619-7181
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29253"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29253&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29253"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29253&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									455 WEST 37TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 643-6090
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30360"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30360&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30360"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30360&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										333 EAST 102ND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 423-2042
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26645"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26645&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26645"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26645&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1350 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 695-6346
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29754"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29754&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29754"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29754&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										333 7TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 239-0167
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21615"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21615&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21615"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21615&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1889 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 586-6749
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25030"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25030&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25030"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25030&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1187 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(917) 432-0634
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24520"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24520&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24520"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24520&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										29-33 7TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 741-3365
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23607"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23607&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23607"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23607&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1467 FIRST AVE. #168<br/>
									
									
									NEW YORK,NY&nbsp;10075	<br/>														
									
									  Phone:&nbsp;(212) 585-2106
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23436"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23436&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23436"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23436&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1290 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 665-8966
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23588"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23588&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23588"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23588&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										60 SPRING ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 925-5307
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23599"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23599&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23599"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23599&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										130 WILLIAM ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 385-1131
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24793"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24793&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24793"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24793&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										949 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 980-0965
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22499"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22499&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22499"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22499&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										852 2ND. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 983-1810
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24403"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24403&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24403"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24403&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										279-283 W. 125TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 663-4391
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22198"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22198&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22198"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22198&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1ST FLOOR<br/>
									
										24 EAST 14TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 989-3639
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22086"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22086&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22086"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22086&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1 UNION SQUARE SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 358-8206
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23639"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23639&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23639"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23639&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1235 LEXINGTON AVE<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 570-2710
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29238"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29238&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29238"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29238&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										661 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 977-1562
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21942"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21942&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21942"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21942&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										41 EAST 58TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 421-4880
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18617"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18617&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18617"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18617&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										99 JOHN STREET<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 791-3801
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18624"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18624&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18624"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18624&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										320 W. 145TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 939-0941
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26229"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26229&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26229"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26229&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										568 W 125TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 334-5329
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29407"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29407&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29407"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29407&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1657 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10119	<br/>														
									
									  Phone:&nbsp;(212) 957-4680
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30980"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30980&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30980"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30980&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										250 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10007	<br/>														
									
									  Phone:&nbsp;(212) 571-4511
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18609"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18609&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18609"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18609&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										401 PARK AVENUE SOUTH<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 213-9730
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18612"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18612&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18612"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18612&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										617 WEST 181ST STREET<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 923-6912
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23737"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23737&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23737"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23737&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										111 WORTH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 571-4621
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25994"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25994&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25994"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25994&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1082 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 223-1130
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24626"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24626&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24626"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24626&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									325 NORTH END AVE<br/>
									
									
									NEW YORK,NY&nbsp;10282	<br/>														
									
									  Phone:&nbsp;(212) 945-4450
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27469"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27469&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27469"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27469&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2108 3RD. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 987-1372
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23716"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23716&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23716"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23716&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										300 EAST 39TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 599-7492
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25327"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25327&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25327"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25327&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										611 AVENUE OF AMERICAS<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 691-0952
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23783"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23783&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23783"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23783&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									1637 YORK AVE<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 534-2000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28491"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28491&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28491"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28491&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										46 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 475-3563
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28121"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28121&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28121"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28121&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										636 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 979-2142
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26862"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26862&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26862"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26862&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										4 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 581-5527
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23570"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23570&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23570"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23570&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										77 7TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 243-2446
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24825"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24825&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24825"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24825&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1524 2ND. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(646) 422-1023
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24534"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24534&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24534"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24534&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										721 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 246-0168
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24536"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24536&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24536"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24536&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										2522 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 663-1580
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22184"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22184&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22184"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22184&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									575 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31165"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31165&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31165"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31165&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									1550 3RD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 838-0195
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30755"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30755&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30755"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30755&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									3387 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(917) 816-5660
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31217"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31217&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31217"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31217&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										305 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10007	<br/>														
									
									  Phone:&nbsp;(212) 227-6168
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18611"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18611&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18611"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18611&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1749-53 FIRST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(646) 672-1760
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26097"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26097&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26097"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26097&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DUANE READE<br/>
									C/O PHARMACY<br/>
									
										1490 MADISON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 410-2508
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27149"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27149&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27149"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27149&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									DUNBAR PHARMACY INC.<br/>
									2580 ADAM CLAYTON POWELL<br/>
									
										JR. BLVD.<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 234-4493
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30381"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30381&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30381"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30381&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									DYNASTY DRUG &amp; TRADING, INC.<br/>
									208 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 226-1415
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18828"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18828&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18828"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18828&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									E CARE PHARMACY CORP<br/>
									48 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 962-3388
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30860"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30860&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30860"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30860&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EAST BROADWAY DRUGS CORP.<br/>
									215 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 420-8642
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31564"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31564&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31564"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31564&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									EAST DRIVE PHARMACY, INC.<br/>
									93 AVE. D<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 228-0400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18037"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18037&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18037"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18037&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EAST END PHARMACY, INC.<br/>
									210 EAST 116TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 831-1730
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25216"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25216&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25216"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25216&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									EAST HARLEM PHARMACY CORP.<br/>
									2095 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(646) 750-3744
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31506"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31506&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31506"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31506&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EAST RX CORP.<br/>
									215 E. BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 420-8642
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20892"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20892&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20892"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20892&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									EAST SIDE PHARMACY, INC.<br/>
									1751 SECOND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(718) 445-5400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24314"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24314&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24314"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24314&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EQUAL CARE PHARMACY, INC<br/>
									753 E 5TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 228-6137
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27486"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27486&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27486"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27486&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ERRI INC.<br/>
									245 EAST 124TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 348-6700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31230"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31230&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31230"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31230&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ERXCITY CORP<br/>
									185 CANAL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 625-8339
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30450"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30450&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30450"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30450&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ESCO DRUG CO., INC.<br/>
									687 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 246-8169
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3599"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3599&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3599"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3599&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ESKAY PHARMACY INC.<br/>
									2101 FIRST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 423-2910
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27621"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27621&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27621"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27621&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ETHICAL DRUG INC.<br/>
									1265 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 781-4214
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30032"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30032&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30032"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30032&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EUREKA LABORATORIES, INC.<br/>
									894 6TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 695-4232
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25353"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25353&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25353"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25353&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									EVE &amp; STEVE PHARMACY, INC.<br/>
									250 EAST HOUSTON STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 677-6688
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26553"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26553&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26553"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26553&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EVEREADY DRUGS LLC<br/>
									1229 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 249-1050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24266"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24266&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24266"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24266&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									EXPRESS DRUGS, INC.<br/>
									126 DYCKMAN ST.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 569-0400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21397"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21397&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21397"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21397&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									EZ CARE PHARMACY LLC<br/>
									87 ELIZABETH STREET<br/>
									
										1ST FLOOR<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 343-8899
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29565"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29565&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29565"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29565&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FAMILY CHOICE PHARMACY CORP.<br/>
									221 CANAL STREET<br/>
									
										2ND FLOOR<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 925-6088
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29676"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29676&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29676"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29676&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FAMILY PHARMACY &amp; SURGICAL INC.<br/>
									379 WEST 125TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 222-1300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25522"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25522&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25522"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25522&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FAMILY PLUS PHARMACY CORP.<br/>
									THE CHINA ARCADE<br/>
									
										14-18 ELIZABETH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 732-3388
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27305"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27305&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27305"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27305&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FARMACIA CENTRAL, INC.<br/>
									102 NAGLE AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 942-5050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29586"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29586&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29586"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29586&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FARMACIA INC.<br/>
									1631 YORK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 737-8800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23934"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23934&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23934"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23934&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FEDERAL EASTERN CHEMISTS LLC.<br/>
									309 COLUMBUS AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 877-3308
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27997"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27997&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27997"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27997&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FEIN'S ETHICAL PHARMACY CORP.<br/>
									3586 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 862-3315
									
								</td>
								
								

								<td> <a  name="PriceLink" id="9097"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=9097&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="9097"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=9097&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FIRST PHARMACEUTICAL CORP.<br/>
									85 ELIZABETH STREET.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 966-7588
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26196"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26196&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26196"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26196&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FOOKANG PHARMACY, INC.<br/>
									139 CENTRE ST.<br/>
									
										APT 201<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 625-8878
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30774"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30774&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30774"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30774&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FOREVER HEALTH PHARMACY I, LLC<br/>
									244 GRAND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30411"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30411&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30411"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30411&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FOREVER HEALTH PHARMACY INC.<br/>
									2 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 966-7887
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29191"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29191&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29191"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29191&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FORUM DRUGS INC.<br/>
									165 WEST 127TH STREET<br/>
									
										#10<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31259"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31259&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31259"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31259&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FOZI, INC.<br/>
									960 AMSTERDAM AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 222-4650
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17349"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17349&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17349"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17349&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									FRS DRUG INC.<br/>
									1475 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 535-4710
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21723"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21723&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21723"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21723&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									FULTON FAMILY PHARMACY INC<br/>
									98 EAST BROADWAY 1F<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 431-6688
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29285"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29285&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29285"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29285&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									G.A.C. PHARMACY CORP.<br/>
									1032 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 755-4244
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30995"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30995&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30995"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30995&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GENERAL CARE PHARMACY, INC.<br/>
									159-A EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 227-7262
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25161"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25161&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25161"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25161&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GENERATION PHARMACY LLC<br/>
									31-33 OLIVER ST<br/>
									
										STORE #3<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 227-9129
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27853"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27853&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27853"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27853&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GENOVESE DRUG STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										495 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 334-0431
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26931"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26931&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26931"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26931&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GENOVESE DRUG STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										250 VESEY ST.<br/>
									
									
									NEW YORK,NY&nbsp;10080	<br/>														
									
									  Phone:&nbsp;(845) 246-2886
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26307"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26307&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26307"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26307&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GENOVESE DRUG STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										1299 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 772-0104
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21855"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21855&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21855"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21855&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GENOVESE DRUG STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										195 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 929-6915
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26942"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26942&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26942"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26942&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GIDEON'S DRUGS, INC.<br/>
									1385 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 575-6868
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26805"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26805&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26805"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26805&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GOOD CARE PHARMACY INC.<br/>
									232A SHERMAN AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 567-1115
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26160"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26160&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26160"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26160&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GOTHAM PHARMACY INC.<br/>
									2258 THIRD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-7800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31845"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31845&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31845"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31845&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GRAMERCY DRUGS INC.<br/>
									214 EAST 23RD. STREET<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 532-0022
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31324"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31324&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31324"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31324&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GRAND HEALTH PHARMACY, INC.<br/>
									349 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 228-0068
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30234"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30234&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30234"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30234&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GRAND STREET PHARMACEUTICAL LLC<br/>
									215-7 GRAND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 625-9505
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28030"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28030&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28030"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28030&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GRISTEDES FOODS, INC.<br/>
									C/O PHARMACY<br/>
									
										80 WEST  END AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(917) 441-5960
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25552"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25552&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25552"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25552&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									GRISTEDES FOODS, INC.<br/>
									1344 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 879-9050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25026"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25026&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25026"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25026&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									GSPM PHARMACY INC.<br/>
									2830 FREDERICK DOUGLAS<br/>
									
										BLVD<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 234-3900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30325"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30325&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30325"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30325&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									H &amp; C CHEMISTS INC.<br/>
									1299 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 535-1700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30730"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30730&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30730"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30730&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									H &amp; J PHARMACEUTICAL INC.<br/>
									1381 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 928-7263
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17199"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17199&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17199"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17199&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HAGH PRESCRIPTION HEADQUARTERS INC.<br/>
									371 1ST. AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 777-6864
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20825"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20825&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20825"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20825&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HAMILTON PHARMACY INC.<br/>
									3293 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 281-0488
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26430"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26430&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26430"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26430&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HAMILTON PRESCRIPTIONS INC.<br/>
									5 HAMILTON PL.<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 281-7121
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15703"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15703&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15703"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15703&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HARLEM DRUGS INC.<br/>
									565 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 281-7276
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25993"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25993&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25993"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25993&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HARLEM HOSPITAL CENTER<br/>
									C/O OUTPATIENT PHARMACY<br/>
									
										530 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 939-8064
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28985"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28985&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28985"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28985&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HARLEM PHARMACY INC.<br/>
									17 WEST 125TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 831-0200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25606"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25606&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25606"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25606&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HARLEM RX INC.<br/>
									102 D E F WEST 116TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 666-8100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30363"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30363&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30363"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30363&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HARLEM STAR PHARMACY INC.<br/>
									67 WEST 137TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 926-7500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29425"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29425&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29425"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29425&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HASHMAT PHARMACY, INC.<br/>
									1654 ST. NICHOLAS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 568-4000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24282"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24282&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24282"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24282&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEALTH CITY PHARMACY CORP.<br/>
									137 MOTT STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 267-8882
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27038"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27038&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27038"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27038&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEALTH RITE PHARMACY INC.<br/>
									1988 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 781-8888
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31185"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31185&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31185"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31185&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEALTH WISE PHARMACY INC.<br/>
									1494 YORK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10075	<br/>														
									
									  Phone:&nbsp;(212) 472-5600
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21341"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21341&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21341"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21341&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEALTHSOURCE PHARMACY II, INC.<br/>
									120 E. 34TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 481-6600
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25501"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25501&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25501"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25501&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEALTHSOURCE PHARMACY III B INC.<br/>
									1000 FIRST AVE<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 310-0111
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30612"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30612&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30612"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30612&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEALTHSOURCE PHARMACY III, INC<br/>
									235 EAST 57TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 794-8700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27524"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27524&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27524"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27524&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEALTHSOURCE PHARMACY, INC.<br/>
									1302 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 794-8700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25135"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25135&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25135"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25135&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEALTHY LIFE PHARMACY INC.<br/>
									77 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 285-0977
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31003"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31003&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31003"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31003&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEALTHY PHARMACY INC.<br/>
									108 BOWERY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 966-8682
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26567"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26567&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26567"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26567&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEIDI PHARMACY INC.<br/>
									522 WEST 181ST STREET<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 740-3737
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31700"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31700&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31700"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31700&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HEIGHTS COMMUNITY PHARMACY, INC.,THE<br/>
									120 AUDUBON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 795-4080
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28398"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28398&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28398"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28398&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HEIGHTS PHARMACY, INC.<br/>
									719 WEST 181ST. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 781-0707
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25669"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25669&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25669"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25669&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HESTER PHARMACY CORP.<br/>
									151-155 HESTER ST<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 966-7599
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29063"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29063&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29063"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29063&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									HLP PHARMCY, INC.<br/>
									3569 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30746"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30746&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30746"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30746&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									HUDSON SQUARE PHARMACY LLC<br/>
									345 HUDSON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 989-1400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29566"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29566&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29566"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29566&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									IEFA LLC.<br/>
									4197 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 795-7455
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31755"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31755&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31755"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31755&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									INWOOD PHARMA INC.<br/>
									4915 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 304-4646
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29975"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29975&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29975"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29975&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									INWOOD PHARMACY, INC.<br/>
									4915 BROADWAY #3,4<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 304-4646
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24544"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24544&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24544"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24544&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ISHAM BROADWAY PHARMACY INC.<br/>
									4996 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 567-3137
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20350"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20350&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20350"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20350&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ISLA DRUG STORES INC.<br/>
									1994 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 427-7123
									
								</td>
								
								

								<td> <a  name="PriceLink" id="13251"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=13251&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="13251"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=13251&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									J. LEON LASCOFF &amp; SON INC.<br/>
									1209 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 288-9500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="1"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=1&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="1"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=1&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									J.BIRDS, INC.<br/>
									855 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 734-5678
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31891"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31891&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31891"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31891&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									J.D. PHARMACY, INC.<br/>
									302 WEST 12TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 929-7527
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20541"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20541&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20541"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20541&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									J.J. COLUMBUS DRUG CO. INC.<br/>
									1009 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 662-6630
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19570"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19570&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19570"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19570&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									J.J. PHARMACY CO., INC.<br/>
									4043 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 795-1240
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18844"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18844&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18844"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18844&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									J.W. EMBASSY CORP.<br/>
									200-210 W. 145TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 368-8100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16953"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16953&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16953"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16953&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JANIK PHARMACY CORP.<br/>
									C/O PHARMACY<br/>
									
										520 WEST 207TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 567-1350
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24305"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24305&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24305"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24305&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JAY PHARMACY CORP.<br/>
									1328 ST NICHOLAS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 568-1383
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29079"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29079&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29079"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29079&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JAYASUDHA INC.<br/>
									767 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 265-8110
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19519"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19519&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19519"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19519&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JED INC.<br/>
									1449 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 517-7500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17952"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17952&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17952"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17952&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JEFFERSON PHARMA LLC<br/>
									210 WEST 145TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10030	<br/>														
									
									  Phone:&nbsp;(347) 952-4747
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31367"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31367&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31367"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31367&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JKM DRUGS INC.<br/>
									1479 ST. NICHOLAS AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 923-4190
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17050"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17050&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17050"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17050&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JMC PHARMACY, INC.<br/>
									3865 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 795-4909
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15799"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15799&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15799"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15799&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JOIA PHARMACY INC.<br/>
									3 WALKER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-0095
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23089"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23089&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23089"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23089&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JOMESSE ENTERPRISES INC<br/>
									2580 SEVENTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 213-8323
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24584"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24584&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24584"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24584&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JRA DRUG CORP.<br/>
									506 W 207TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 304-0101
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28965"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28965&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28965"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28965&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									JUSTIN PHARMACY INC.<br/>
									3860 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 923-6111
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26695"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26695&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26695"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26695&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									JVJ PHARMACY INC.<br/>
									74 UNIVERSITY PLACE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 473-0277
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26955"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26955&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26955"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26955&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									K &amp; R UNITED CORP.<br/>
									227 AVENUE B<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 505-1788
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24945"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24945&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24945"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24945&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									KARNABY CHEMISTS, INC.<br/>
									407 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 475-5760
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25667"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25667&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25667"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25667&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									KINGS THIRD AVE. PHARMACY, INC.<br/>
									1619 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 534-9244
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25191"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25191&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25191"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25191&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									KINGS TRIBECA PHARMACY, INC.<br/>
									5 HUDSON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 791-3100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23690"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23690&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23690"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23690&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									KMART CORPORATION<br/>
									C/O PHARMACY<br/>
									
										1 PENN PLAZA<br/>
									
									
										250 WEST 34TH ST.<br/>
									
									NEW YORK,NY&nbsp;10119	<br/>														
									
									  Phone:&nbsp;(212) 760-1242
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23053"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23053&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23053"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23053&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									KMART CORPORATION<br/>
									C/O PHARMACY DEPT.<br/>
									
										770 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 253-9661
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23094"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23094&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23094"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23094&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									L &amp; V PHARMACY INC.<br/>
									99 NASSAU ST.<br/>
									
										STORE 111<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 962-4900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31138"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31138&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31138"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31138&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									L.D.C. PHARMACY CORP.<br/>
									1901 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 369-5555
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16369"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16369&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16369"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16369&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LA ALTAGRACIA PHARMACY, INC.<br/>
									1544 A ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 795-5004
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17806"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17806&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17806"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17806&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LA HISPANA ON BROADWAY PHARMACY, LLC<br/>
									3890 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 568-6878
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29488"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29488&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29488"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29488&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LADA PHARMACY INC.<br/>
									3 EAST 115TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 722-0100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31380"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31380&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31380"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31380&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LC PHARMACY INC.<br/>
									75 EAST BROADWAY<br/>
									
										SOUTH BUILDING<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 513-1177
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31098"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31098&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31098"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31098&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LENDA PHARMACY, INC.<br/>
									3397 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 368-3130
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15501"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15501&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15501"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15501&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LENOX DRUG CORP<br/>
									523 LENOX AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 281-7408
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31252"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31252&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31252"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31252&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LENOX HILL PHARMACY INC.<br/>
									1103 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 879-0910
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23694"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23694&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23694"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23694&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LENOX PHARMACY INC.<br/>
									27 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 678-9722
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23095"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23095&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23095"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23095&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LENOX STAR PHARMACY INC.<br/>
									531 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 368-7900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30815"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30815&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30815"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30815&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LENOX SUPER PHARMACY INC.<br/>
									685 LENOX AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31234"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31234&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31234"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31234&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LENOX TERRACE II LLC.<br/>
									480A LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31208"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31208&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31208"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31208&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LENOX TERRACE PHARMACY, INC.<br/>
									20 WEST 135TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 234-2050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25372"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25372&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25372"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25372&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LERIN DRUG CO., INC.<br/>
									501 WEST 113TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 678-0636
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17529"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17529&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17529"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17529&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LEX DRUGS INC.<br/>
									1797 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 426-0402
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25909"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25909&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25909"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25909&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LEXINGTON AVENUE PHARMACY, INC.<br/>
									2056 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 426-5555
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30023"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30023&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30023"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30023&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LEXINGTON CHEMISTS, INC.<br/>
									806 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 838-2500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21266"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21266&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21266"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21266&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LEXINGTON HEALTHCARE INC.<br/>
									1570 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31286"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31286&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31286"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31286&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LGDK LLC<br/>
									752 ST. NICHOLAS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 281-8300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27351"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27351&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27351"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27351&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LIFE PHARMA II INC.<br/>
									471 LENOX AVE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 694-5700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29019"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29019&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29019"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29019&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LISALISA, INC.<br/>
									2330 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 724-1950
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25491"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25491&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25491"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25491&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									LOISAIDA RX, INC.<br/>
									273 EAST THIRD ST.<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 254-7307
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25186"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25186&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25186"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25186&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									LONGEVITY PHARMACY LLC<br/>
									96 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 693-8866
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28788"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28788&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28788"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28788&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									M &amp; D PHARMACY, LLC<br/>
									17 WEST 125TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 831-0200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29773"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29773&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29773"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29773&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MADISON AVENUE PHARMACY INC.<br/>
									1407 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 722-3200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20222"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20222&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20222"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20222&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MADISON CHEMIST, INC<br/>
									1412 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 996-9499
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20466"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20466&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20466"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20466&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MADISON DRUGS INC.<br/>
									36 GOUVERNEUR ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 385-6775
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24861"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24861&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24861"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24861&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MAIL MED CORP.<br/>
									11 PENN PLAZA<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 279-3232
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27411"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27411&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27411"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27411&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MAKSOUD RX CORP.<br/>
									800 2ND AVE<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(646) 918-7363
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30598"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30598&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30598"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30598&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MALCOLM PHARMACY,INC.<br/>
									160 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 722-1550
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25096"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25096&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25096"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25096&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MALCOLM X PHARMACY CORP.<br/>
									523 LENOX AVE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 281-7408
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27852"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27852&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27852"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27852&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MANAV II INC.<br/>
									449 W 125TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 665-6007
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26778"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26778&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26778"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26778&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MANHATTAN CHINATOWN PHARMACY INC.<br/>
									156 CANAL STREET<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 233-2833
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31285"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31285&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31285"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31285&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MANHATTANVILLE PHARMACY INC.<br/>
									567 W. 125TH ST.<br/>
									
										STORE #2<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 222-3576
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28829"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28829&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28829"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28829&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MANNINGS PHARMACY CORPORATION<br/>
									13-17 ELIZABETH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 941-6480
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20841"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20841&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20841"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20841&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MANNYRX, INC.<br/>
									4953 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 569-1230
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28803"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28803&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28803"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28803&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MATLAND PHARMACY CORP.<br/>
									1142 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 744-4144
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19327"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19327&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19327"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19327&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MAXWELL PHARMACY INC<br/>
									234 EAST 106TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 534-7700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27755"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27755&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27755"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27755&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MEDIEXPRESS PHARMACY CORP.<br/>
									78 CLINTON STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 386-9886
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27286"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27286&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27286"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27286&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MEDILANE PHARMACY CORP.<br/>
									204 CLINTON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 571-2888
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23258"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23258&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23258"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23258&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MEDPHARM DRUG &amp; TRADING, INC.<br/>
									61 CATHERINE ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 267-5670
									
								</td>
								
								

								<td> <a  name="PriceLink" id="20043"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=20043&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="20043"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=20043&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MELBRAN DRUGS, INC.<br/>
									605 WEST 168TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 568-1300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27613"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27613&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27613"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27613&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MELLAU PHARMACY INC.<br/>
									593 FT. WASHINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 568-5511
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22914"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22914&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22914"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22914&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									METRO DRUGS 14TH ST. CORP.<br/>
									7 WEST 14TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 627-7315
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24928"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24928&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24928"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24928&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									METRO DRUGS 3RD AVE. CORP.<br/>
									931 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 794-7200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21108"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21108&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21108"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21108&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									METRO DRUGS 8TH ST. CORP.<br/>
									13 EAST 8TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 982-7325
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24340"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24340&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24340"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24340&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									METROCARE RX , INC.<br/>
									59 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 608-8889
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30864"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30864&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30864"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30864&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									METROPHARM INC.<br/>
									92 BAXTER ST., B2<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-8668
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21451"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21451&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21451"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21451&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									METROPOLITAN PHARMACY INC.<br/>
									1982 2ND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 831-1000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24128"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24128&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24128"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24128&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									METROPOLITAN PHARMACY SERVICES INC.<br/>
									532 LAGUARDIA PLACE<br/>
									
										SUITE 313<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 253-7459
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25071"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25071&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25071"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25071&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MIDTOWN EAST PHARMACY &amp; SURGICAL LLC<br/>
									161 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 213-2444
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29513"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29513&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29513"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29513&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MNK PHARMACY INC.<br/>
									181 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 877-6390
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21250"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21250&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21250"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21250&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MNS PHARMACY CORP<br/>
									2201 AMSTERDAM AVENUE<br/>
									
										#B2<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(646) 559-1515
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30741"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30741&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30741"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30741&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MODERN CHEMIST, LLC, THE<br/>
									189 7TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;11215	<br/>														
									
									  Phone:&nbsp;(718) 369-6100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29737"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29737&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29737"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29737&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MORNINGSIDE PHARMACY, INC.<br/>
									3181 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 662-0220
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16840"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16840&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16840"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16840&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									MORRIS PHARMACY INC.<br/>
									1419 AVE. OF THE AMERICAS<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 247-1538
									
								</td>
								
								

								<td> <a  name="PriceLink" id="3972"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=3972&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="3972"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=3972&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									MSSC PHARMACY INC.<br/>
									4407 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 543-2333
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29095"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29095&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29095"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29095&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NAGLE PHARMACY INC.<br/>
									220 NAGLE AVE.<br/>
									
										STORE #8<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 942-0202
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29587"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29587&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29587"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29587&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NAMDOR INC.<br/>
									227 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 807-0950
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24849"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24849&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24849"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24849&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NAMDOR INC.<br/>
									C/O PHARMACY<br/>
									
										460 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 251-0052
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28785"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28785&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28785"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28785&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NATES PHARMACY CORP<br/>
									205 THIRD AVE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31489"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31489&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31489"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31489&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NATURES CURE PHARMACY INC.<br/>
									324 EAST 34TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 545-9393
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28288"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28288&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28288"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28288&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NATURES FIRST PHARMACY CORP.<br/>
									313 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 228-7900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31526"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31526&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31526"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31526&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NEW AMSTERDAM DRUG MART, INC.<br/>
									C/O PHARMACY<br/>
									
										698 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 865-9700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18173"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18173&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18173"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18173&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NEW LONDON PHARMACY INC.<br/>
									246 8TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 243-4987
									
								</td>
								
								

								<td> <a  name="PriceLink" id="8530"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=8530&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="8530"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=8530&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NEW YORK HEALTH FIRST PHARMACY INC.<br/>
									2021 1ST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 987-0700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31135"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31135&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31135"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31135&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NEW YORK PHARMACY, INC.<br/>
									131 WALKER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-3287
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27143"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27143&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27143"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27143&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NEW YORK RX, INC.<br/>
									875 THIRD AVE<br/>
									
										2ND FLOOR M105<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 838-3606
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28337"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28337&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28337"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28337&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NEWMAN-LYMAN DRUG CO., INC.<br/>
									3901 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 923-7617
									
								</td>
								
								

								<td> <a  name="PriceLink" id="9930"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=9930&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="9930"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=9930&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NIHAR CORP.<br/>
									850 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 678-0084
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26068"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26068&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26068"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26068&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NKS PHARMACY INC.<br/>
									50 UNIVERSITY PLACE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 473-4166
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22821"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22821&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22821"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22821&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NMS DRUGS INC.<br/>
									199 DYCKMAN STREET<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 567-1331
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26627"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26627&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26627"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26627&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NOLITA DRUG CORPORATION<br/>
									208 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 226-1415
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31924"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31924&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31924"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31924&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NORTH STAR PHARMACY INC.<br/>
									2253 3RD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 426-6200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31731"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31731&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31731"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31731&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NUCARE PHARMACY INC.<br/>
									1789 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29549"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29549&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29549"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29549&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NUCARE PHARMACY WEST, LLC<br/>
									250 NINTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 462-2525
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29957"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29957&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29957"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29957&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NUTRI-PHARMA INC.<br/>
									6 EAST 46TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 983-8291
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21653"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21653&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21653"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21653&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NY FIRST AVE. CORPORATION<br/>
									206 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 253-8686
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24531"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24531&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24531"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24531&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NYC CHELSEA PHARMACY INC.<br/>
									215 WEST 14TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31627"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31627&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31627"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31627&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									NYC PHARMACY INC.<br/>
									203 EAST 121ST STREET<br/>
									
										STORE #2<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-8082
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25666"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25666&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25666"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25666&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									NYCO DRUGS, INC.<br/>
									485 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 486-9543
									
								</td>
								
								

								<td> <a  name="PriceLink" id="16198"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=16198&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="16198"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=16198&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									OLIVE TREE PHARMACY LLC<br/>
									106 RIDGE ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(646) 368-9960
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29889"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29889&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29889"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29889&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									OMEGA PHARMACY, INC<br/>
									1439 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 234-4666
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28220"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28220&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28220"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28220&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ONE SOURCE PHARMACY SERVICES INC.<br/>
									4480 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 567-3384
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24844"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24844&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24844"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24844&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									P DRUGS INC.<br/>
									2345 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 877-0888
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30018"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30018&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30018"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30018&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PALACE PHARMACY INC<br/>
									543 LENOX AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 283-2136
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27539"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27539&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27539"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27539&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PANCARE PHARMACY, INC.<br/>
									22 BOWERY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 240-2312
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26165"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26165&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26165"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26165&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PARK AVENUE CHEMISTS LTD.<br/>
									1080 PARK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 289-5866
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17867"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17867&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17867"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17867&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PARK IRMAT DRUG CORP.<br/>
									2 PARK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 685-0500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21645"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21645&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21645"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21645&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PARVJAYRON CORP.<br/>
									1329 ST. NICHOLAS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 795-3033
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29148"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29148&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29148"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29148&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PATHMARK STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										300 WEST 145TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 281-3480
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27057"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27057&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27057"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27057&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PATHMARK STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										237-239 CHERRY ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 227-3520
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17977"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17977&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17977"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17977&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PATHMARK STORES, INC.<br/>
									C/O PHARMACY<br/>
									
										160 EAST 125TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 722-9156
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23710"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23710&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23710"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23710&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PAYLESS RX PHARMACY, INC.<br/>
									567 WEST 207TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 544-0020
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31066"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31066&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31066"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31066&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PD ENTERPRISES INC.<br/>
									909 COLUMBUS AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 222-6388
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26608"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26608&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26608"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26608&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PEOPLE CHOICE PHARMACY INC<br/>
									527 GRAND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 388-0888
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27713"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27713&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27713"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27713&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PERSONAL PHARMACY INC.<br/>
									4873 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 942-8785
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30356"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30356&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30356"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30356&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PETER'S PHARMACY AND VITAMINS INC.<br/>
									652 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 873-8838
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25831"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25831&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25831"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25831&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PHARMA CARE INC.<br/>
									2454 ADAM CLAYTON<br/>
									
										POWELL BLVD<br/>
									
									
									NEW YORK,NY&nbsp;10030	<br/>														
									
									  Phone:&nbsp;(212) 862-0505
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29301"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29301&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29301"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29301&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PHARMACARE SERVICES INC.<br/>
									483 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 696-2044
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25603"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25603&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25603"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25603&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PHARMACO, INC.<br/>
									216B CANAL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 513-1344
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21547"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21547&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21547"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21547&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PHARMAX INC.<br/>
									207 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 343-1252
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25584"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25584&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25584"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25584&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									POLLOCK-BAILEY APOTHECARY, LTD.<br/>
									405 EAST 57TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 755-4244
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15678"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15678&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15678"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15678&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PRANAYA PHARMACY, INC.<br/>
									586 LENOX AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 368-3777
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24680"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24680&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24680"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24680&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PRIME ESSENTIALS LLC<br/>
									345 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 941-7900
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30587"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30587&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30587"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30587&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PRO + LIFE APOTHECARY CORP.<br/>
									1235 1ST AVE<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 628-1110
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27558"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27558&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27558"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27558&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PROCARE PHARMACY, L.L.C<br/>
									C/O PHARMACY<br/>
									
										126 EIGHTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 807-8798
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24813"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24813&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24813"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24813&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PROCARE PHARMACY, L.L.C<br/>
									C/O PHARMACY<br/>
									
										138 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 254-7760
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19202"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19202&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19202"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19202&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									PROCARE PHARMACY, L.L.C.<br/>
									C/O PHARMACY<br/>
									
										892 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 445-0932
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24572"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24572&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24572"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24572&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									PROHEALTH PHARMACY, INC.<br/>
									385 A/B SECOND AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 684-8300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24569"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24569&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24569"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24569&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									R.G. DRUG CORP.<br/>
									2201 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 877-3480
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21514"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21514&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21514"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21514&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									R.O.R. MADISON PHARMACY, INC<br/>
									1636 MADISON AVE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 369-0700
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27675"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27675&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27675"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27675&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RAM PHARMACY INC<br/>
									146 NAGLE AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 304-0649
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24636"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24636&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24636"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24636&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RAPHAEL DRUG AND HEALTH, LTD.<br/>
									1257 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 684-0090
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15725"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15725&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15725"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15725&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RAYSOL DRUGS INC.<br/>
									1870 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 348-2117
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17020"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17020&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17020"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17020&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RDS PHARMACY, INC.<br/>
									225 MADISON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 227-5227
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27146"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27146&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27146"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27146&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID DRUG PALACE, INC.<br/>
									C/O PHARMACY<br/>
									
										408 GRAND STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 529-7115
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19388"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19388&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19388"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19388&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										1033 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 795-3218
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26806"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26806&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26806"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26806&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										2551 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 222-5824
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22625"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22625&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22625"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22625&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										188 9TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 727-9620
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22823"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22823&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22823"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22823&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										309 WEST 125TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 961-1246
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22282"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22282&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22282"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22282&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										2712 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 665-6200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23017"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23017&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23017"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23017&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										501 6TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 727-3720
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22972"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22972&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22972"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22972&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										3539 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 281-2183
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22858"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22858&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22858"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22858&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										301 WEST 50TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 247-8384
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24241"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24241&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24241"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24241&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										2833 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 663-3135
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22811"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22811&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22811"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22811&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										282 8TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10001	<br/>														
									
									  Phone:&nbsp;(212) 727-3854
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22466"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22466&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22466"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22466&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY         .<br/>
									
										546-558 WEST 207TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 942-1883
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22305"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22305&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22305"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22305&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										516 E. 14TH ST. &amp; AVE. A<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 979-2455
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22672"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22672&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22672"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22672&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										35-45 WEST 125TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 828-1772
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24267"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24267&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24267"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24267&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										2155 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 534-9781
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23663"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23663&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23663"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23663&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										1535 2ND. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 327-4757
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22859"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22859&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22859"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22859&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										542-576 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 213-9887
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24248"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24248&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24248"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24248&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										1510 ST NICHOLAS AVE<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(917) 521-7814
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24385"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24385&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24385"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24385&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										26 GRAND CENTRAL TERMINAL<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 972-8052
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24606"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24606&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24606"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24606&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										56 SEVENTH AVE &amp; 14TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 675-1697
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22581"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22581&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22581"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22581&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										81 1ST. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 388-9348
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22817"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22817&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22817"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22817&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										1951 1ST. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 360-5530
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27261"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27261&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27261"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27261&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										4188 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 791-5396
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27687"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27687&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27687"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27687&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										4910 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 569-2512
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22619"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22619&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22619"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22619&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										210-20 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 787-2903
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22618"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22618&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22618"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22618&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										1849 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10128	<br/>														
									
									  Phone:&nbsp;(212) 828-8664
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23206"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23206&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23206"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23206&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										741 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 316-0436
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22660"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22660&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22660"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22660&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										7 MADISON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 791-5795
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23757"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23757&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23757"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23757&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										2170 FREDERICK DOUGLASS<br/>
									
									
										BLVD.<br/>
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 666-3013
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27138"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27138&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27138"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27138&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										4046 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 928-2550
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24613"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24613&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24613"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24613&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										87-89 AVENUE D<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 475-5315
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22369"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22369&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22369"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22369&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RITE AID OF NEW YORK, INC.<br/>
									C/O PHARMACY<br/>
									
										534 HUDSON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(646) 486-1048
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24542"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24542&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24542"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24542&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RITE HOPE PHARMACY INC.<br/>
									1793A MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 348-3341
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29922"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29922&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29922"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29922&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RIVERSIDE PHARMACY INC.<br/>
									2920 8TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 491-5500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26816"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26816&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26816"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26816&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RIVERSIDE SRX INC.<br/>
									2920 FREDERICK DOUGLAS<br/>
									
										BLVD.<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 491-5500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30384"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30384&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30384"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30384&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RIVINGTON HOUSE HEALTH CARE FACILITY<br/>
									C/O PHARMACY<br/>
									
										45 RIVINGTON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 477-3100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22229"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22229&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22229"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22229&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ROBELEN CHEMISTS, INC.<br/>
									100 PARK AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 682-2817
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21483"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21483&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21483"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21483&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RON-AN PHARMACY, INC.<br/>
									988 FIRST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 755-6632
									
								</td>
								
								

								<td> <a  name="PriceLink" id="14934"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=14934&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="14934"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=14934&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ROSA PHARMACY, INC.<br/>
									1603 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 923-2412
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25087"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25087&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25087"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25087&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ROYAL CARE PHARMACY, INC.<br/>
									127 EAST 110TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 996-0055
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29790"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29790&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29790"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29790&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ROYAL DRUGS CORP<br/>
									5030 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31549"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31549&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31549"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31549&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RVK PHARMACY, LTD.<br/>
									170 DYCKMAN ST.<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 568-2246
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29272"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29272&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29272"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29272&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RX 2000, INC.<br/>
									2325 FIRST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-8839
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19566"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19566&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19566"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19566&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RX NOW II, INC.<br/>
									565 LENOX AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10037	<br/>														
									
									  Phone:&nbsp;(212) 368-5800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30058"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30058&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30058"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30058&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RX NOW INC.<br/>
									1728 AMSTERDAM AVE<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 368-3759
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29081"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29081&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29081"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29081&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									RX PLUS PHARMACY CORP.<br/>
									289 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 274-0009
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22511"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22511&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22511"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22511&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									RYAN DRUGS, LLC<br/>
									850 AMSTERDAM AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 678-0084
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29680"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29680&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29680"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29680&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									S &amp; J PHARMACY CORP.<br/>
									3921 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 928-6342
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24760"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24760&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24760"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24760&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									S &amp; Y DRUG, INC.<br/>
									1714 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 926-2801
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17959"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17959&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17959"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17959&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									S H DRUGS INC.<br/>
									220 NAGLE AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 942-0202
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31674"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31674&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31674"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31674&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									S.B.P. PHARMACY CORP.<br/>
									312 W. 14TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 727-7979
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24776"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24776&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24776"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24776&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SANTA ISABEL PHARMACY INC.<br/>
									145 SHERMAN AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 567-1448
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30989"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30989&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30989"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30989&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SB PHARMACY, INC.<br/>
									27-29 EAST 124TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 534-2849
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25342"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25342&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25342"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25342&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SBV PHARMACY CORP.<br/>
									217 EAST 106TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 534-1939
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24737"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24737&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24737"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24737&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SECOND AVE PHARMACY INC.<br/>
									249 EAST 115TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 876-8300
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26821"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26821&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26821"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26821&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SECOND AVE. CHEMISTS INC.<br/>
									101 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 473-1587
									
								</td>
								
								

								<td> <a  name="PriceLink" id="4177"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=4177&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="4177"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=4177&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SEVENTH ELM DRUG CORP<br/>
									56 SEVENTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 255-6100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30275"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30275&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30275"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30275&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SHREE NATH PHARMACY CORP.<br/>
									1576 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 795-1795
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22714"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22714&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22714"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22714&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SHRINEETA PHARMACY INC.<br/>
									1743 AMSTERDAM AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 234-7959
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26316"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26316&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26316"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26316&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SKYLINE PHARMACY INC.<br/>
									2123 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10020	<br/>														
									
									  Phone:&nbsp;(212) 996-5929
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31567"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31567&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31567"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31567&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SMART PHARMACY INC.<br/>
									55 WEST 39TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10018	<br/>														
									
									  Phone:&nbsp;(212) 398-9999
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31978"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31978&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31978"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31978&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SMS PHARMACY CORP.<br/>
									101 SHERMAN AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 567-2753
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22261"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22261&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22261"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22261&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SR PHARMACY INC<br/>
									4329 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 740-8500
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27473"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27473&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27473"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27473&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SSS PHARMACY INC.<br/>
									66 NAGLE AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 304-3949
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31103"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31103&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31103"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31103&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									ST. LUKE'S ROOSEVELT HOSPITAL CENTER<br/>
									230 WEST 17TH ST 8TH FLR<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 604-1970
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30198"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30198&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30198"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30198&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ST. THERESA PHARMACY CORP<br/>
									3849 10TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 304-4541
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31005"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31005&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31005"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31005&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									STANLEY'S PHARMACY INC.<br/>
									31 LUDLOW STREET<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31765"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31765&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31765"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31765&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									SVR INC.<br/>
									159-12 HARLEM RIVER DRIVE<br/>
									
									
									NEW YORK,NY&nbsp;10039	<br/>														
									
									  Phone:&nbsp;(212) 283-7200
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26505"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26505&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26505"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26505&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									SY PHARMACY INC.<br/>
									215 WEST 116TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10026	<br/>														
									
									  Phone:&nbsp;(212) 665-8880
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30720"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30720&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30720"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30720&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TAINO STAR PHARMACY, INC.<br/>
									2403 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 289-2000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28756"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28756&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28756"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28756&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TARIQ, NAJMUT &amp; SADEQUIN, MOHAMMAD<br/>
									RAHMAN, MOHAMMED TARIQUR<br/>
									
										CROSS COUNTY PHARMACY<br/>
									
									
										1514 MADISON AVE.<br/>
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 360-6969
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18765"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18765&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18765"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18765&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TEE VAL PHARMACY, INC.<br/>
									104 W. 70TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 877-3090
									
								</td>
								
								

								<td> <a  name="PriceLink" id="4240"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=4240&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="4240"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=4240&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									THIRD AVE PHARMACY INC.<br/>
									2240 3RD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10035	<br/>														
									
									  Phone:&nbsp;(212) 837-2692
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30846"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30846&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30846"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30846&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									THIRD AVE. PHARMACY &amp; SURGICALS, INC.<br/>
									550 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 447-6111
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21243"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21243&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21243"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21243&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									THIRD AVE. PRESCRIPTION CENTER, INC.<br/>
									2032 THIRD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 369-6075
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23429"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23429&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23429"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23429&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									THIRD AVENUE DRUG CORP<br/>
									1449 1ST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 535-7100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29197"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29197&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29197"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29197&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									THIRD AVENUE LERMAN PHARMACEUTICS, INC.<br/>
									1025-A THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 750-4100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26361"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26361&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26361"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26361&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									THOMAS DRUGS, INC.<br/>
									171 COLUMBUS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10023	<br/>														
									
									  Phone:&nbsp;(212) 877-7340
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22429"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22429&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22429"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22429&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									THOMPSON CHEMISTS INC.<br/>
									137 THOMPSON ST.<br/>
									
									
									NEW YORK,NY&nbsp;10012	<br/>														
									
									  Phone:&nbsp;(212) 598-9790
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22226"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22226&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22226"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22226&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									THRIFTWAY 10TH AVE. DRUG CORP.<br/>
									646 TENTH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 956-1100
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28807"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28807&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28807"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28807&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									THRIFTWAY BEEKMAN PHARMACY, INC.<br/>
									19 BEEKMAN ST.<br/>
									
									
									NEW YORK,NY&nbsp;10038	<br/>														
									
									  Phone:&nbsp;(212) 766-1942
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19846"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19846&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19846"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19846&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TIMMERMANN APOTHECARIES, INC.<br/>
									799 LEXINGTON AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 838-6450
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17119"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17119&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17119"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17119&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TISANE PHARMACY LLC<br/>
									340 EAST 86 ST.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;0
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30789"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30789&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30789"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30789&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TOTAL HEALTH &amp; BEAUTY PHARMACY INC.<br/>
									4873 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 942-8785
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22920"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22920&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22920"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22920&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TOWER CHEMISTS INC.<br/>
									1219 1ST AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 838-1490
									
								</td>
								
								

								<td> <a  name="PriceLink" id="9886"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=9886&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="9886"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=9886&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TOWN DRUG AT BROADWAY INC.<br/>
									4785 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10034	<br/>														
									
									  Phone:&nbsp;(212) 304-9582
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22829"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22829&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22829"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22829&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TRI PHARMACY CORP.<br/>
									1219 AMSTERDAM AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 749-8480
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28256"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28256&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28256"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28256&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TRIGUN PHARMACY INC.<br/>
									178 AVENUE C.<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 228-0764
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17378"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17378&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17378"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17378&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TRUSTEES OF COLUMBIA UNIVERSITY IN THE CITY<br/>
									OF NEW YORK, THE<br/>
									
										C/O PHARMACY - ROOM IP749<br/>
									
									
										161 FT. WASHINGTON AVE<br/>
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 305-8684
									
								</td>
								
								

								<td> <a  name="PriceLink" id="23275"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=23275&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="23275"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=23275&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TU QUYNH PHARMACY, INC.<br/>
									230 GRAND STREET<br/>
									
										BOOTH A1 AND A2<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 219-8998
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27214"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27214&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27214"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27214&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TURTLE BAY CHEMISTS EAST, INC.<br/>
									901 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10017	<br/>														
									
									  Phone:&nbsp;(212) 752-5151
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17340"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17340&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17340"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17340&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									TWIN PHARMACY CORP<br/>
									1538 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 927-5570
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30285"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30285&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30285"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30285&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									TYKA HOLDINGS INC.<br/>
									173 CANAL ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 343-1517
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29441"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29441&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29441"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29441&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									UMA PHARMACY CORP.<br/>
									446 6TH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 477-0762
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22526"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22526&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22526"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22526&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									UNITED HEALTH PHARMACY INC.<br/>
									4 ELIZABETH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 766-3773
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24143"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24143&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24143"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24143&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									UPPER MANHATTAN PHARMACY, INC.<br/>
									1728 AMSTERDAM AVE<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 694-6666
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30615"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30615&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30615"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30615&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									UPTOWN PHARMACY &amp; SURGICALS INC.<br/>
									4027 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 923-6000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27696"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27696&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27696"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27696&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									V.L.V. MED PHARMACY, INC.<br/>
									4085 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 923-7530
									
								</td>
								
								

								<td> <a  name="PriceLink" id="18488"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=18488&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="18488"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=18488&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VALUE DRUGS ROCK INC.<br/>
									30 ROCKEFELLER CENTER<br/>
									
									
									NEW YORK,NY&nbsp;10020	<br/>														
									
									  Phone:&nbsp;(212) 757-9335
									
								</td>
								
								

								<td> <a  name="PriceLink" id="21812"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=21812&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="21812"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=21812&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									VBVS PHARMACY INC.<br/>
									1200 FIRST AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 734-6998
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31131"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31131&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31131"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31131&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VENKANY, INC.<br/>
									2452 8TH AVE<br/>
									
									
									NEW YORK,NY&nbsp;10027	<br/>														
									
									  Phone:&nbsp;(212) 283-9114
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27035"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27035&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27035"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27035&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									VENUS PHARMACY &amp; SUPPLIES, CORP.<br/>
									972 AMSTERDAM AVE<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 666-4800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28454"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28454&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28454"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28454&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VIDA PHARMACY, INC.<br/>
									1620 ST. NICHOLA AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 923-3524
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28789"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28789&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28789"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28789&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									VILLAGE APOTHECARY, INC.<br/>
									346 BLEECKER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 807-7566
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17656"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17656&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17656"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17656&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VILLAGE PHARMACY CORP.<br/>
									346 BLEECKER ST.<br/>
									
									
									NEW YORK,NY&nbsp;10014	<br/>														
									
									  Phone:&nbsp;(212) 807-7566
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31690"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31690&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31690"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31690&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									VILLY PHARMACY, INCORPORATED<br/>
									179 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 226-8971
									
								</td>
								
								

								<td> <a  name="PriceLink" id="22843"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=22843&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="22843"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=22843&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VIM CHEMIST INC.<br/>
									766 WEST 181ST STREET<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 795-4383
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25533"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25533&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25533"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25533&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									VITA HEALTH APOTHECARY INC.<br/>
									1609 2ND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 772-1110
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29888"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29888&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29888"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29888&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									VIVA PHARMACY, INC.<br/>
									1494 ST. NICHOLAS AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10033	<br/>														
									
									  Phone:&nbsp;(212) 923-0077
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19952"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19952&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19952"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19952&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									W &amp; Z DRUGS INC.<br/>
									39 SHERMAN AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10040	<br/>														
									
									  Phone:&nbsp;(212) 567-5533
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19639"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19639&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19639"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19639&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EAST CO., INC<br/>
									122 EAST 86TH ST<br/>
									
									
									NEW YORK,NY&nbsp;10028	<br/>														
									
									  Phone:&nbsp;(212) 427-3868
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28854"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28854&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28854"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28854&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC<br/>
									C/O PHARMACY<br/>
									
										545 THIRD AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10016	<br/>														
									
									  Phone:&nbsp;(212) 696-5081
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28876"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28876&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28876"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28876&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC<br/>
									C/O PHARMACY<br/>
									
										2575 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10025	<br/>														
									
									  Phone:&nbsp;(212) 678-8556
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28943"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28943&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28943"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28943&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									197 8TH AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10011	<br/>														
									
									  Phone:&nbsp;(212) 691-9050
									
								</td>
								
								

								<td> <a  name="PriceLink" id="31226"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=31226&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="31226"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=31226&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									353 W. 57TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 315-0178
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29477"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29477&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29477"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29477&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										1328 2ND. AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 734-6076
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27113"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27113&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27113"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27113&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										1000 SECOND AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10022	<br/>														
									
									  Phone:&nbsp;(212) 752-1909
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28397"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28397&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28397"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28397&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										145 FOURTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 677-0054
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25100"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25100&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25100"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25100&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										298 1ST AVE<br/>
									
									
									NEW YORK,NY&nbsp;10009	<br/>														
									
									  Phone:&nbsp;(212) 777-0740
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27965"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27965&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27965"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27965&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									1471 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10036	<br/>														
									
									  Phone:&nbsp;(212) 302-0552
									
								</td>
								
								

								<td> <a  name="PriceLink" id="29200"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=29200&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="29200"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=29200&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									1160 THIRD AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10065	<br/>														
									
									  Phone:&nbsp;(212) 861-0291
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28538"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28538&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28538"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28538&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										350 FIFTH AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10118	<br/>														
									
									  Phone:&nbsp;(212) 868-5659
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25307"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25307&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25307"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25307&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									C/O PHARMACY<br/>
									
										33 EAST 23RD. ST.<br/>
									
									
									NEW YORK,NY&nbsp;10010	<br/>														
									
									  Phone:&nbsp;(212) 685-1641
									
								</td>
								
								

								<td> <a  name="PriceLink" id="26363"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=26363&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="26363"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=26363&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WALGREEN EASTERN CO., INC.<br/>
									20 ASTOR PLACE<br/>
									
									
									NEW YORK,NY&nbsp;10003	<br/>														
									
									  Phone:&nbsp;(212) 375-0734
									
								</td>
								
								

								<td> <a  name="PriceLink" id="28702"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=28702&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="28702"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=28702&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WELLNESS RX PHARMACY INC.<br/>
									206 GRAND ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30813"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30813&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30813"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30813&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WEST 142ND STREET PHARMACY CORP.<br/>
									3471 BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10031	<br/>														
									
									  Phone:&nbsp;(212) 234-8400
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30934"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30934&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30934"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30934&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WEST SIDE FAMILY PHARMACY, INC.<br/>
									592 AMSTERDAM AVENUE<br/>
									
									
									NEW YORK,NY&nbsp;10024	<br/>														
									
									  Phone:&nbsp;(212) 712-0818
									
								</td>
								
								

								<td> <a  name="PriceLink" id="24479"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=24479&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="24479"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=24479&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WIN PHARMACY CORP<br/>
									11 EDWARD MORGAN PLACE<br/>
									
									
									NEW YORK,NY&nbsp;10032	<br/>														
									
									  Phone:&nbsp;(212) 234-1800
									
								</td>
								
								

								<td> <a  name="PriceLink" id="30168"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=30168&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="30168"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=30168&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									WING ON PHARMACY, INC.<br/>
									16-18 EAST BROADWAY<br/>
									
									
									NEW YORK,NY&nbsp;10002	<br/>														
									
									  Phone:&nbsp;(212) 219-2717
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19881"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19881&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19881"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19881&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									WINMARK DRUG, LTD.<br/>
									1065 LEXINGTON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 737-1280
									
								</td>
								
								

								<td> <a  name="PriceLink" id="17370"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=17370&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="17370"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=17370&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									YIN ON PHARMACY, INC.<br/>
									77 MOTT ST.<br/>
									
									
									NEW YORK,NY&nbsp;10013	<br/>														
									
									  Phone:&nbsp;(212) 285-0977
									
								</td>
								
								

								<td> <a  name="PriceLink" id="15718"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=15718&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="15718"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=15718&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									YOUR HEALTH PHARMACY, INC.<br/>
									76-80 EAST 116TH ST.<br/>
									
									
									NEW YORK,NY&nbsp;10029	<br/>														
									
									  Phone:&nbsp;(212) 348-7788
									
								</td>
								
								

								<td> <a  name="PriceLink" id="25832"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=25832&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="25832"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=25832&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="">
								<td> 
								    
									Z CHEMISTS, LLC<br/>
									40 WEST 57TH STREET<br/>
									
									
									NEW YORK,NY&nbsp;10019	<br/>														
									
									  Phone:&nbsp;(212) 956-6000
									
								</td>
								
								

								<td> <a  name="PriceLink" id="27202"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=27202&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="27202"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=27202&calledFrom=searchPharmacy"> View </a></td>
							</tr>
																			
							<tr class="tableRowEven">
								<td> 
								    
									ZITOMER PHARMACY INC.<br/>
									969 MADISON AVE.<br/>
									
									
									NEW YORK,NY&nbsp;10021	<br/>														
									
									  Phone:&nbsp;(212) 737-5560
									
								</td>
								
								

								<td> <a  name="PriceLink" id="19328"  href="/pdpw/Pharmacy/Price/PriceList.action?sedRegNum=19328&calledFrom=searchPharmacy"> View </a></td>
								<td> <a name="MapLink"  id="19328"  href="/pdpw/ViewMap/ShowMap.action?sedRegNum=19328&calledFrom=searchPharmacy"> View </a></td>
							</tr>
							
						</table>			
					</td>
				</tr>
			</table>
		
	</div>
	</form>




</div>


		</div>
		<div id="footer"> 
	<div id="email">
		<a href="/pdpw/Contact.action" title="Contact Us" >   Send us your feedback</a>
	</div>
	<div id="reviseddate">Revised: May 2010</div>
	<div id="footerbuttons">
		<ul >
			<li><a href="https://www.health.ny.gov/nysdoh/disclaim.htm" >Disclaimer</a></li>
			<li><a href="https://www.health.ny.gov/nysdoh/privacy.htm" >Privacy Policy</a></li>
			<li><a href="/pdpw/Version.action" title="Version Information" >Version</a></li>
		</ul>
	</div>
</div>

	</body>
</html>'''

pharmacies = htmlcopy.split('<tr class')
index = -2

for pharmacytxt in pharmacies:
  index = index + 1
  
  # skip first row with column names
  if index == -1:
    pharmacies[0] = None
    continue

  # cut off HTML beyond last row
  if(pharmacytxt.find('</table>') > -1):
    pharmacytxt = pharmacytxt[ : pharmacytxt.find('</table>') ]

  pharmacy = { }
  pharmacy["name"] = ""
  pharmacy["address"] = ""
  pharmacy["phone"] = ""
  pharmacy["zip"] = ""
  pharmacy["id"] = ""
  
  details = pharmacytxt.split('<br/>')
  myid = pharmacytxt[ pharmacytxt.find('sedRegNum=') + 10 : ]
  pharmacy["id"] = myid[ : myid.find('&') ]
  
  namepart = details[0].split('\t')
  pharmacy["name"] = namepart[ len(namepart) - 1 ]
  #pharmacy["address"] = pharmacy["name"]
  
  detailnum = -1
  
  for detail in details:
    detailnum = detailnum + 1
    if(detailnum == 0):
      continue
      
    # don't include C/O PHARMACY in address
    if(detail.find('C/O PHARMACY') > -1):
      continue
  
    if(detail.find("Phone:") > -1):
      pharmacy["phone"] = detail.split('&nbsp;')[1].split('\r')[0].split('\n')[0]
    else:
      # some address information
      if(pharmacy["address"] != ""):
        pharmacy["address"] = pharmacy["address"] + ", "
      pharmacy["address"] = pharmacy["address"] + detail.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;',' ').replace('&amp;','&').split('<')[0]
      
      # capture zip
      if(detail.find("NY&nbsp;") > -1):
        pharmacy["zip"] = detail.split('&nbsp;')[1].split('	')[0]

  #print pharmacy

  # replace text with object
  pharmacies[index+1] = pharmacy
  

output = "json"

if(output == "csv"):
  # print '"ID","Name","Address","Zip","Phone"'
  for pharmacy in pharmacies:
    if pharmacy is None:
      continue
    p = [
      pharmacy["id"],
      pharmacy["name"],
      pharmacy["address"],
      pharmacy["zip"],
      pharmacy["phone"]
    ]
    print '"' + '","'.join(p) + '"'
elif(output == "json"):
  print json.dumps( pharmacies )