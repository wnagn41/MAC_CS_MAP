








// Criteria
var locations=new Array();
var showOnlineDropdown = false;
var feeReportButton = false;
var template = "mcm";
var preopenCampusSelector = false;

var baseUri = "https://csprd.mcmaster.ca/psp/prcsprd/";
var bookstoreUri = "";
var signInUrl = "";
var minLengthOfCrn = 4;
var autoCompleteSize = 20;
var defaultCamsPerTerm = {"null":"MCMSTiSNPOL_MCMSTiMHK_MCMSTiMCMST_MCMSTiOFF_MCMSTiCON_"};

var defaultCams = defaultCamsPerTerm[null]?defaultCamsPerTerm[null]:"";
var gtimezone = "America/New_York";
var otimezone = "America/New_York";
var oredirect = "http://localhost:8080/vsb/outlook.jsp";
var oclient_id = "7f6eed1c-a826-4d4b-807a-f2107af92e31";
var gclient_id = "447488977917-s5i2anhjqeu33j713df42v12tta13anh.apps.googleusercontent.com";
var isAuthenticated= false;
var isAuthentication = true;
var defaultSchoolTermId = 0;
var hideUncheckedClassNotes = false;
var guidanceOkSessions = "1,DYN,7W1,7W2";
var hideGuidance = false;
var selectTermIf1 = false;
var holdWelcome = false;
var fullPageWelcome = false;
var fullPageSearch = false;
var neverShowFilterStep = true;
var boldMultiSelectItems = "";
var termChangeLossWarning = true;
var hideCourseReqInCriteria = false;
var notDroppedWarning = true;
var hideAttrsInCourse = false;
var pauseResults = false;
var showPeriodWithDisp = false;
var enablePeriodDropdown = true;
var showPeriodIfOne = true;
var showMoreOn = false;
var permitInstantDrop = false;
var breakOutOfIframe = false;
var autoSuggestSelCamsOnly = false;
var dwAuditInstitutions = "";
var dwAuditApiPullOnDemand = false;
var dwSepInstitutions = "";
var dwSepApiPullOnDemand = false;
var noSelectWhenGuest = false;
var showNonBlockingHolds = false;
var generalizeSortHomeCampToCollege = false;
var blockUserByGlobalHold = false;
var showTermNameInTermBox = false;
var showLowCostTextbookLabel = false;
var onlineClassIcon = "far fa-mouse";
var preventTermIfNoActivation = false;
var matchSessionLessThanOrEqual = false;

// Results
var minDuration = 0;
var crnHelpText = "true";
var minCampusSwitchTime = 45;
var warnPsLocationSwitchInstead = false;
var warnLocationSwitchInstead = false;
var onlineClassCampusChangeWarning = false;
var switchTimeOverrides = [];
var extraLinks = [];
var enrollType = "real";
var enrollTypeWhenAdvising = "none";
var resetCurrentResult=false;
var showFullCampusInLegend=true;
var enableCohort = false;
var timesheetHourHeight = 0;
var useSeatNumbers = true;
var showRecommendationNumbers = false;
var weekSliderDisplay = true;
var minFullTimeCredits = 0.0;
var maxFullTimeCredits = 0.0;
var positiveWaitlistFillsClass = false;
var noSwapSupport = false;
var inspecificSeats = true;
var disableRel12Parenthesis = false;
var institution = "MCMST";
var sendNonEnrolledOnly = false;
var hideOffCampusDefault = false;
var showHoursInLegend = true;
var offCampusFilter = false; // Not in use. Placeholder for new filter.
var onReservedFilter = false;
var uselSortRule = "taken";
var selSortRule = "taken";
var minSeatsTakenPercToPromote = 30;
var defaultHideFullClasses = true;
var fullFilter = true;
var allowDualSchedule = true;
var dualScheduleAlwaysIfMultiYear = true;
var locationOnTimetable = false;
var datesOnTimetable = false;
var secNoOnTimetable = false;
var hideOpenEnrollmentDate = false;
var dispCrnInsteadOfSection = false;
var descReplacements = [];
var hiddenInstructionalMethods = {};
var calendarStart = 11;
var calendarEnd = 13;

var alwaysShowWaitlist = false;
var hideWaitlistFromLegend = false;
var showReserveCapacities = false;
var hideCapsNotNow = true;
var hideDisplayStringClassType = false;
var showCourseReqInLegend = true;
var hideAssReqInLegend = false;
var notYetEnrolledNotice = true;
var hideDropOfHue =  false;
var hideAttrsInLegend = false;
var fullOnViewResults = true;
var defaultRecShowType = "all";
var dontCollapseSimilar = false;
var defaultNoCollapse = true;
var individualClassStatus = true;
var hideCapsStartDate = true;
var hideCapsEndDate = true;
var randomizeLegendSelection = false;
var maximizeSwap = false;
var countNonEnrolledEECredits = false;
var advisorCantAdviseSelf = false;
var advisorCanBypassTermBlock = false;
var advisorsSeeHue = false;
var defaultSort = "none";
var legendOnByDefault = true;
var extNotesInLegend = false;
var largeDateGrid = false;
var hideReqInLegendIfAllSame = false;
var legendAttrValDisp = false;
var legendAttrBold = [];
var legendAttrFirst = [];
var enforceMaxCohortness =  false;
var wildcardDefaultNoSelection = false;
var hideAPUnits = false;
var conditionalAddDrop = false;
var confirmActions = false;
var hideTimetable = false;

// Shared Auth
var authenticated = false;
var isAuthenticatedWithSso = false;
var isConfigurator = false;
var isAdvisor = false;
var isScheduler = false;
var isAdvising = false;
var userPidm = null;
var userId = "GUEST_698a5aaa-c7a4-4cff-a360-3a2e5056235a";
var advisee = null;
var adviseePidm = null;
var adviseeId = null;
var analyticsAccess = false;
var hideSelfConflicting =  false;
var hideRepeatSecNo = false;
var onlyRemainingSeats = false;
var hideManualPersonalTimes = false;

// Shared
var switchNameAndCode = false;
var template = "mcm";
var guestMode = true;
var todayCode = 6222;

var preventOutOfEnrollmentWindow = false;
var useLeafCartItemId = false;
var hideCrn = false;
var disableHotkeys = false;
var vsbDatabase = true;
var displayLocationOption = true;
var filterCollege = false;
var filterCampus = false;
var filterLocation = true;
var filterInstruct = true;
var filterSession = false;
var filterInstructSortReverse = false;
var alphanumSessionsSort = false;
var hideCnfCheckboxes = false;
var username = "null";
var disableCart = false; // default only
var disableEnroll = false; // default only
var cartValidation = true;
var waitlistableFilter = false;
var recommendScheduleEnabled = true;
var hideRecommendationDisplay = false;
var recommendKnownUserOnly = false;
var showPlansOnWelcome = false;
var maxFavorites = 3;
var noSelectCourseLogic = "";
var coursesToHideFromSelect = "";
var coursesLocked = "";
var hideCoursesLogic = '';
var oneShotEnrollment = false;
var hideCourseToggleCheckbox = false;
var altHRMS = "HRMS";
var shortUrl = true;
var forceCartValidation = false;
var useInstitutionAsCampus = false;
var blockUserBasedOnAttribute = "";
var csvImportInstitutions = "";
var disablePsLogoutCheck = false;
var welcomeActionLink = "";
var blockTimeInterval = 60;
var coursesToIgnoreForHasEnrolled = "";

var terms=new Array();

// Analytics
var analyticsFiltersIncludeCode = false;
terms.push("3202420");terms.push("3202430");terms.push("3202510");




var visibleCampuses = "";


var disableAnalyticsSortFilters = false;


var displayCourseRegisterLink = false;
var displayStudentSectionAuthorization = false;


var locationCategory = '';

