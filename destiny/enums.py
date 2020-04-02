from enum import IntEnum

class ApplicationScopes(IntEnum):
    ReadBasicUserProfile = 1
    ReadGroups = 2
    WriteGroups = 4
    AdminGroups = 8
    BnetWrite = 16
    MoveEquipDestinyItems = 32
    ReadDestinyInventoryAndVault = 64
    ReadUserData = 128
    EditUserData = 256
    ReadDestinyVendorsAndAdvisors = 512
    ReadAndApplyTokens = 1024
    AdvancedWriteActions = 2048
    PartnerOfferGrant = 4096

class OAuthApplicationType(IntEnum):
    Null = 0
    Confidential = 1
    Public = 2

class ApplicationStatus(IntEnum):
    Null = 0
    Private = 1
    Public = 2
    Disabled = 3
    Blocked = 4

class DeveloperRole(IntEnum):
    Null = 0
    Owner = 1
    TeamMember = 2

class BungieMembershipType(IntEnum):
    Null = 0
    TigerXbox = 1
    TigerPsn = 2
    TigerSteam = 3
    TigerBlizzard = 4
    TigerStadia = 5
    TigerDemon = 10
    BungieNext = 254
    All = -1

class IgnoreStatus(IntEnum):
    NotIgnored = 0
    IgnoredUser = 1
    IgnoredGroup = 2
    IgnoredByGroup = 4
    IgnoredPost = 8
    IgnoredTag = 16
    IgnoredGlobal = 32

class BungieCredentialType(IntEnum):
    Null = 0
    Xuid = 1
    Psnid = 2
    Wlid = 3
    Fake = 4
    Facebook = 5
    Google = 8
    Windows = 9
    DemonId = 10
    SteamId = 12
    BattleNetId = 14
    StadiaId = 16
    TwitchId = 18

class ContentPropertyDataTypeIntEnum(IntEnum):
    Null = 0
    Plaintext = 1
    Html = 2
    Dropdown = 3
    List = 4
    Json = 5
    Content = 6
    Representation = 7
    Set = 8
    File = 9
    FolderSet = 10
    Date = 11
    MultilinePlaintext = 12
    DestinyContent = 13
    Color = 14

class ForumTopicsCategoryFiltersIntEnum(IntEnum):
    Null = 0
    Links = 1
    Questions = 2
    AnsweredQuestions = 4
    Media = 8
    TextOnly = 16
    Announcement = 32
    BungieOfficial = 64
    Polls = 128

class ForumTopicsQuickDateIntEnum(IntEnum):
    All = 0
    LastYear = 1
    LastMonth = 2
    LastWeek = 3
    LastDay = 4

class ForumTopicsSortIntEnum(IntEnum):
    Default = 0
    LastReplied = 1
    MostReplied = 2
    Popularity = 3
    Controversiality = 4
    Liked = 5
    HighestRated = 6
    MostUpvoted = 7

class ForumMediaType(IntEnum):
    Null = 0
    Image = 1
    Video = 2
    Youtube = 3

class ForumPostPopularity(IntEnum):
    Empty = 0
    Default = 1
    Discussed = 2
    CoolStory = 3
    HeatingUp = 4
    Hot = 5

class ForumPostCategoryIntEnums(IntEnum):
    Null = 0
    TextOnly = 1
    Media = 2
    Link = 4
    Poll = 8
    Question = 16
    Answered = 32
    Announcement = 64
    ContentComment = 128
    BungieOfficial = 256
    NinjaOfficial = 512
    Recruitment = 1024

class ForumFlagsIntEnum(IntEnum):
    Null = 0
    BungieStaffPost = 1
    ForumNinjaPost = 2
    ForumMentorPost = 4
    TopicBungieStaffPosted = 8
    TopicBungieVolunteerPosted = 16
    QuestionAnsweredByBungie = 32
    QuestionAnsweredByNinja = 64
    CommunityContent = 128

class GroupType(IntEnum):
    General = 0
    Clan = 1

class ChatSecuritySetting(IntEnum):
    Group = 0
    Admins = 1

class GroupHomepage(IntEnum):
    Wall = 0
    Forum = 1
    AllianceForum = 2

class MembershipOption(IntEnum):
    Reviewed = 0
    Open = 1
    Closed = 2

class GroupPostPublicity(IntEnum):
    Public = 0
    Alliance = 1
    Private = 2

class Capabilities(IntEnum):
    Null = 0
    Leaderboards = 1
    Callsign = 2
    OptionalConversations = 4
    ClanBanner = 8
    D2InvestmentData = 16
    Tags = 32
    Alliances = 64

class HostGuidedGamesPermissionLevel(IntEnum):
    Null = 0
    Beginner = 1
    Member = 2

class RuntimeGroupMemberType(IntEnum):
    Null = 0
    Beginner = 1
    Member = 2
    Admin = 3
    ActingFounder = 4
    Founder = 5

class DestinyProgressionRewardItemState(IntEnum):
    Null = 0
    Invisible = 1
    Earned = 2
    Claimed = 4
    ClaimAllowed = 8

class DestinyProgressionScope(IntEnum):
    Account = 0
    Character = 1
    Clan = 2
    Item = 3
    ImplicitFromEquipment = 4
    Mapped = 5
    MappedAggregate = 6
    MappedStat = 7
    MappedUnlockValue = 8

class DestinyProgressionStepDisplayEffect(IntEnum):
    Null = 0
    Character = 1
    Item = 2

class TierType(IntEnum):
    Unknown = 0
    Currency = 1
    Basic = 2
    Common = 3
    Rare = 4
    Superior = 5
    Exotic = 6

class BucketScope(IntEnum):
    Character = 0
    Account = 1

class BucketCategory(IntEnum):
    Invisible = 0
    Item = 1
    Currency = 2
    Equippable = 3
    Ignored = 4

class ItemLocation(IntEnum):
    Unknown = 0
    Inventory = 1
    Vault = 2
    Vendor = 3
    Postmaster = 4

class DestinyStatAggregationType(IntEnum):
    CharacterAverage = 0
    Character = 1
    Item = 2

class DestinyStatCategory(IntEnum):
    Gameplay = 0
    Weapon = 1
    Defense = 2
    Primary = 3

class EquippingItemBlockAttributes(IntEnum):
    Null = 0
    EquipOnAcquire = 1

class DestinyAmmunitionType(IntEnum):
    Null = 0
    Primary = 1
    Special = 2
    Heavy = 3
    Unknown = 4

class VendorDisplayCategorySortOrder(IntEnum):
    Default = 0
    SortByTier = 1

class DestinyVendorInteractionRewardSelection(IntEnum):
    Null = 0
    One = 1
    All = 2

class DestinyVendorReplyType(IntEnum):
    Accept = 0
    Decline = 1
    Complete = 2

class VendorInteractionType(IntEnum):
    Unknown = 0
    Undefined = 1
    QuestComplete = 2
    QuestContinue = 3
    ReputationPreview = 4
    RankUpReward = 5
    TokenTurnIn = 6
    QuestAccept = 7
    ProgressTab = 8
    End = 9
    Start = 10

class DestinyItemSortType(IntEnum):
    ItemId = 0
    Timestamp = 1
    StackSize = 2

class DestinyVendorItemRefundPolicy(IntEnum):
    NotRefundable = 0
    DeletesItem = 1
    RevokesLicense = 2

class DestinyGatingScope(IntEnum):
    Null = 0
    Global = 1
    Clan = 2
    Profile = 3
    Character = 4
    Item = 5
    AssumedWorstCase = 6

class SocketTypeActionType(IntEnum):
    InsertPlug = 0
    InfuseItem = 1
    ReinitializeSocket = 2

class DestinySocketVisibility(IntEnum):
    Visible = 0
    Hidden = 1
    HiddenWhenEmpty = 2
    HiddenIfNoPlugsAvailable = 3

class DestinySocketCategoryStyle(IntEnum):
    Unknown = 0
    Reusable = 1
    Consumable = 2
    Unlockable = 3
    Intrinsic = 4
    EnergyMeter = 5
    LargePerk = 6

class ActivityGraphNodeHighlightType(IntEnum):
    Null = 0
    Normal = 1
    Hyper = 2
    Comet = 3
    RiseOfIron = 4

class directActivityModeType(IntEnum):
    Null = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    Reserved9 = 9
    Control = 10
    Reserved11 = 11
    Clash = 12
    Reserved13 = 13
    CrimsonDoubles = 15
    Nightfall = 16
    HeroicNightfall = 17
    AllStrikes = 18
    IronBanner = 19
    Reserved20 = 20
    Reserved21 = 21
    Reserved22 = 22
    Reserved24 = 24
    AllMayhem = 25
    Reserved26 = 26
    Reserved27 = 27
    Reserved28 = 28
    Reserved29 = 29
    Reserved30 = 30
    Supremacy = 31
    PrivateMatchesAll = 32
    Survival = 37
    Countdown = 38
    TrialsOfTheNine = 39
    Social = 40
    TrialsCountdown = 41
    TrialsSurvival = 42
    IronBannerControl = 43
    IronBannerClash = 44
    IronBannerSupremacy = 45
    ScoredNightfall = 46
    ScoredHeroicNightfall = 47
    Rumble = 48
    AllDoubles = 49
    Doubles = 50
    PrivateMatchesClash = 51
    PrivateMatchesControl = 52
    PrivateMatchesSupremacy = 53
    PrivateMatchesCountdown = 54
    PrivateMatchesSurvival = 55
    PrivateMatchesMayhem = 56
    PrivateMatchesRumble = 57
    HeroicAdventure = 58
    Showdown = 59
    Lockdown = 60
    Scorched = 61
    ScorchedTeam = 62
    Gambit = 63
    AllPvECompetitive = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHunt = 79
    Elimination = 80
    Momentum = 81
    Dungeon = 82
    Sundial = 83
    TrialsOfOsiris = 84

class DestinyUnlockValueUIStyle(IntEnum):
    Automatic = 0
    Fraction = 1
    Checkbox = 2
    Percentage = 3
    DateTime = 4
    FractionFloat = 5
    Integer = 6
    TimeDuration = 7
    Hidden = 8
    Multiplier = 9
    GreenPips = 10
    RedPips = 11
    ExplicitPercentage = 12
    RawFloat = 13

class DestinyObjectiveGrantStyle(IntEnum):
    WhenIncomplete = 0
    WhenComplete = 1
    Always = 2

class DamageType(IntEnum):
    Null = 0
    Kinetic = 1
    Arc = 2
    Thermal = 3
    Void = 4
    Raid = 5

class DestinyTalentNodeStepWeaponPerformances(IntEnum):
    Null = 0
    RateOfFire = 1
    Damage = 2
    Accuracy = 4
    Range = 8
    Zoom = 16
    Recoil = 32
    Ready = 64
    Reload = 128
    HairTrigger = 256
    AmmoAndMagazine = 512
    TrackingAndDetonation = 1024
    ShotgunSpread = 2048
    ChargeTime = 4096
    All = 8191

class DestinyTalentNodeStepImpactEffects(IntEnum):
    Null = 0
    ArmorPiercing = 1
    Ricochet = 2
    Flinch = 4
    CollateralDamage = 8
    Disorient = 16
    HighlightTarget = 32
    All = 63

class DestinyTalentNodeStepGuardianAttributes(IntEnum):
    Null = 0
    Stats = 1
    Shields = 2
    Health = 4
    Revive = 8
    AimUnderFire = 16
    Radar = 32
    Invisibility = 64
    Reputations = 128
    All = 255

class DestinyTalentNodeStepLightAbilities(IntEnum):
    Null = 0
    Grenades = 1
    Melee = 2
    MovementModes = 4
    Orbs = 8
    SuperEnergy = 16
    SuperMods = 32
    All = 63

class DestinyTalentNodeStepDamageTypes(IntEnum):
    Null = 0
    Kinetic = 1
    Arc = 2
    Solar = 4
    Void = 8
    All = 15

class DestinyActivityNavPointType(IntEnum):
    Inactive = 0
    PrimaryObjective = 1
    SecondaryObjective = 2
    TravelObjective = 3
    PublicEventObjective = 4
    AmmoCache = 5
    PointTypeFlag = 6
    CapturePoint = 7
    DefensiveEncounter = 8
    GhostInteraction = 9
    KillAi = 10
    QuestItem = 11
    PatrolMission = 12
    Incoming = 13
    ArenaObjective = 14
    AutomationHint = 15
    TrackedQuest = 16

class DestinyActivityModeType(IntEnum):
    Null = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    Reserved9 = 9
    Control = 10
    Reserved11 = 11
    Clash = 12
    Reserved13 = 13
    CrimsonDoubles = 15
    Nightfall = 16
    HeroicNightfall = 17
    AllStrikes = 18
    IronBanner = 19
    Reserved20 = 20
    Reserved21 = 21
    Reserved22 = 22
    Reserved24 = 24
    AllMayhem = 25
    Reserved26 = 26
    Reserved27 = 27
    Reserved28 = 28
    Reserved29 = 29
    Reserved30 = 30
    Supremacy = 31
    PrivateMatchesAll = 32
    Survival = 37
    Countdown = 38
    TrialsOfTheNine = 39
    Social = 40
    TrialsCountdown = 41
    TrialsSurvival = 42
    IronBannerControl = 43
    IronBannerClash = 44
    IronBannerSupremacy = 45
    ScoredNightfall = 46
    ScoredHeroicNightfall = 47
    Rumble = 48
    AllDoubles = 49
    Doubles = 50
    PrivateMatchesClash = 51
    PrivateMatchesControl = 52
    PrivateMatchesSupremacy = 53
    PrivateMatchesCountdown = 54
    PrivateMatchesSurvival = 55
    PrivateMatchesMayhem = 56
    PrivateMatchesRumble = 57
    HeroicAdventure = 58
    Showdown = 59
    Lockdown = 60
    Scorched = 61
    ScorchedTeam = 62
    Gambit = 63
    AllPvECompetitive = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHunt = 79
    Elimination = 80
    Momentum = 81
    Dungeon = 82
    Sundial = 83
    TrialsOfOsiris = 84

class DestinyActivityModeCategory(IntEnum):
    Null = 0
    PvE = 1
    PvP = 2
    PvECompetitive = 3

class DestinyItemSubType(IntEnum):
    Null = 0
    Crucible = 1
    Vanguard = 2
    Exotic = 5
    AutoRifle = 6
    Shotgun = 7
    Machinegun = 8
    HandCannon = 9
    RocketLauncher = 10
    FusionRifle = 11
    SniperRifle = 12
    PulseRifle = 13
    ScoutRifle = 14
    Crm = 16
    Sidearm = 17
    Sword = 18
    Mask = 19
    Shader = 20
    Ornament = 21
    FusionRifleLine = 22
    GrenadeLauncher = 23
    SubmachineGun = 24
    TraceRifle = 25
    HelmetArmor = 26
    GauntletsArmor = 27
    ChestArmor = 28
    LegArmor = 29
    ClassArmor = 30
    Bow = 31

class DestinyGraphNodeState(IntEnum):
    Hidden = 0
    Visible = 1
    Teaser = 2
    Incomplete = 3
    Completed = 4

class DestinyRewardSourceCategory(IntEnum):
    Null = 0
    Activity = 1
    Vendor = 2
    Aggregate = 3

class DestinyPresentationNodeType(IntEnum):
    Default = 0
    Category = 1
    Collectibles = 2
    Records = 3
    Metric = 4

class DestinyScope(IntEnum):
    Profile = 0
    Character = 1

class DestinyPresentationDisplayStyle(IntEnum):
    Category = 0
    Badge = 1
    Medals = 2
    Collectible = 3
    Record = 4

class DestinyRecordValueStyle(IntEnum):
    Integer = 0
    Percentage = 1
    Milliseconds = 2
    Boolean = 3
    Decimal = 4

class DestinyGender(IntEnum):
    Male = 0
    Female = 1
    Unknown = 2

class DestinyRecordToastStyle(IntEnum):
    Null = 0
    Record = 1
    Lore = 2
    Badge = 3
    MetaRecord = 4
    MedalComplete = 5

class DestinyPresentationScreenStyle(IntEnum):
    Default = 0
    CategorySets = 1
    Badge = 2

class PlugUiStyles(IntEnum):
    Null = 0
    Masterwork = 1

class PlugAvailabilityMode(IntEnum):
    Normal = 0
    UnavailableIfSocketContainsMatchingPlugCategory = 1
    AvailableIfSocketContainsMatchingPlugCategory = 2

class DestinyEnergyType(IntEnum):
    Any = 0
    Arc = 1
    Thermal = 2
    Void = 3

class SocketPlugSources(IntEnum):
    Null = 0
    InventorySourced = 1
    ReusablePlugItems = 2
    ProfilePlugSet = 4
    CharacterPlugSet = 8

class ItemPerkVisibility(IntEnum):
    Visible = 0
    Disabled = 1
    Hidden = 2

class SpecialItemType(IntEnum):
    Null = 0
    SpecialCurrency = 1
    Armor = 8
    Weapon = 9
    Engram = 23
    Consumable = 24
    ExchangeMaterial = 25
    MissionReward = 27
    Currency = 29

class DestinyItemType(IntEnum):
    Null = 0
    Currency = 1
    Armor = 2
    Weapon = 3
    Message = 7
    Engram = 8
    Consumable = 9
    ExchangeMaterial = 10
    MissionReward = 11
    QuestStep = 12
    QuestStepComplete = 13
    Emblem = 14
    Quest = 15
    Subclass = 16
    ClanBanner = 17
    Aura = 18
    Mod = 19
    Dummy = 20
    Ship = 21
    Vehicle = 22
    Emote = 23
    Ghost = 24
    Package = 25
    Bounty = 26
    Wrapper = 27
    SeasonalArtifact = 28
    Finisher = 29

class DestinyClass(IntEnum):
    Titan = 0
    Hunter = 1
    Warlock = 2
    Unknown = 3

class DestinyBreakerType(IntEnum):
    Null = 0
    ShieldPiercing = 1
    Disruption = 2
    Stagger = 3

class DestinyProgressionRewardItemAcquisitionBehavior(IntEnum):
    Instant = 0
    PlayerClaimRequired = 1

class GroupAllianceStatus(IntEnum):
    Unallied = 0
    Parent = 1
    Child = 2

class GroupPotentialMemberStatus(IntEnum):
    Null = 0
    Applicant = 1
    Invitee = 2

class ForumRecruitmentIntensityLabel(IntEnum):
    Null = 0
    Casual = 1
    Professional = 2

class ForumRecruitmentToneLabel(IntEnum):
    Null = 0
    FamilyFriendly = 1
    Rowdy = 2

class ForumPostSortIntEnum(IntEnum):
    Default = 0
    OldestFirst = 1

class GroupDateRange(IntEnum):
    All = 0
    PastDay = 1
    PastWeek = 2
    PastMonth = 3
    PastYear = 4

class groupMemberCountFilter(IntEnum):
    All = 0
    OneToTen = 1
    ElevenToOneHundred = 2
    GreaterThanOneHundred = 3

class GroupSortBy(IntEnum):
    Name = 0
    Date = 1
    Popularity = 2
    Id = 3

class GroupMemberCountFilter(IntEnum):
    All = 0
    OneToTen = 1
    ElevenToOneHundred = 2
    GreaterThanOneHundred = 3

class membershipOption(IntEnum):
    Reviewed = 0
    Open = 1
    Closed = 2

class chatSecurity(IntEnum):
    Group = 0
    Admins = 1

class homepage(IntEnum):
    Wall = 0
    Forum = 1
    AllianceForum = 2

class defaultPublicity(IntEnum):
    Public = 0
    Alliance = 1
    Private = 2

class HostGuidedGamePermissionOverride(IntEnum):
    Null = 0
    Beginner = 1
    Member = 2

class JoinLevel(IntEnum):
    Null = 0
    Beginner = 1
    Member = 2
    Admin = 3
    ActingFounder = 4
    Founder = 5

class IgnoreLength(IntEnum):
    Null = 0
    Week = 1
    TwoWeeks = 2
    ThreeWeeks = 3
    Month = 4
    ThreeMonths = 5
    SixMonths = 6
    Year = 7
    Forever = 8
    ThreeMinutes = 9
    Hour = 10
    ThirtyDays = 11

class GroupApplicationResolveState(IntEnum):
    Unresolved = 0
    Accepted = 1
    Denied = 2
    Rescinded = 3

class PlatformErrorCodes(IntEnum):
    Null = 0
    Success = 1
    TransportException = 2
    UnhandledException = 3
    NotImplemented = 4
    SystemDisabled = 5
    FailedToLoadAvailableLocalesConfiguration = 6
    ParameterParseFailure = 7
    ParameterInvalidRange = 8
    BadRequest = 9
    AuthenticationInvalid = 10
    DataNotFound = 11
    InsufficientPrivileges = 12
    Duplicate = 13
    UnknownSqlResult = 14
    ValidationError = 15
    ValidationMissingFieldError = 16
    ValidationInvalidInputError = 17
    InvalidParameters = 18
    ParameterNotFound = 19
    UnhandledHttpException = 20
    NotFound = 21
    WebAuthModuleAsyncFailed = 22
    InvalidReturnValue = 23
    UserBanned = 24
    InvalidPostBody = 25
    MissingPostBody = 26
    ExternalServiceTimeout = 27
    ValidationLengthError = 28
    ValidationRangeError = 29
    JsonDeserializationError = 30
    ThrottleLimitExceeded = 31
    ValidationTagError = 32
    ValidationProfanityError = 33
    ValidationUrlFormatError = 34
    ThrottleLimitExceededMinutes = 35
    ThrottleLimitExceededMomentarily = 36
    ThrottleLimitExceededSeconds = 37
    ExternalServiceUnknown = 38
    ValidationWordLengthError = 39
    ValidationInvisibleUnicode = 40
    ValidationBadNames = 41
    ExternalServiceFailed = 42
    ServiceRetired = 43
    UnknownSqlException = 44
    UnsupportedLocale = 45
    InvalidPagIntEnumber = 46
    MaximumPageSizeExceeded = 47
    ServiceUnsupported = 48
    ValidationMaximumUnicodeCombiningCharacters = 49
    ValidationMaximumSequentialCarriageReturns = 50
    PerEndpointRequestThrottleExceeded = 51
    AuthContextCacheAssertion = 52
    ExPlatformStringValidationError = 53
    PerApplicationThrottleExceeded = 54
    PerApplicationAnonymousThrottleExceeded = 55
    PerApplicationAuthenticatedThrottleExceeded = 56
    PerUserThrottleExceeded = 57
    PayloadSignatureVerificationFailure = 58
    InvalidServiceAuthContext = 59
    ObsoleteCredentialType = 89
    UnableToUnPairMobileApp = 90
    UnableToPairMobileApp = 91
    CannotUseMobileAuthWithNonMobileProvider = 92
    MissingDeviceCookie = 93
    FacebookTokenExpired = 94
    AuthTicketRequired = 95
    CookieContextRequired = 96
    UnknownAuthenticationError = 97
    BungieNetAccountCreationRequired = 98
    WebAuthRequired = 99
    ContentUnknownSqlResult = 100
    ContentNeedUniquePath = 101
    ContentSqlException = 102
    ContentNotFound = 103
    ContentSuccessWithTagAddFail = 104
    ContentSearchMissingParameters = 105
    ContentInvalidId = 106
    ContentPhysicalFileDeletionError = 107
    ContentPhysicalFileCreationError = 108
    ContentPerforceSubmissionError = 109
    ContentPerforceInitializationError = 110
    ContentDeploymentPackageNotReadyError = 111
    ContentUploadFailed = 112
    ContentTooManyResults = 113
    ContentInvalidState = 115
    ContentNavigationParentNotFound = 116
    ContentNavigationParentUpdateError = 117
    DeploymentPackageNotEditable = 118
    ContentValidationError = 119
    ContentPropertiesValidationError = 120
    ContentTypeNotFound = 121
    DeploymentPackageNotFound = 122
    ContentSearchInvalidParameters = 123
    ContentItemPropertyAggregationError = 124
    DeploymentPackageFileNotFound = 125
    ContentPerforceFileHistoryNotFound = 126
    ContentAssetZipCreationFailure = 127
    ContentAssetZipCreationBusy = 128
    ContentProjectNotFound = 129
    ContentFolderNotFound = 130
    ContentPackagesInconsistent = 131
    ContentPackagesInvalidState = 132
    ContentPackagesInconsistentType = 133
    ContentCannotDeletePackage = 134
    ContentLockedForChanges = 135
    ContentFileUploadFailed = 136
    ContentNotReviewed = 137
    ContentPermissionDenied = 138
    ContentInvalidExternalUrl = 139
    ContentExternalFileCannotBeImportedLocally = 140
    ContentTagSaveFailure = 141
    ContentPerforceUnmatchedFileError = 142
    ContentPerforceChangelistResultNotFound = 143
    ContentPerforceChangelistFileItemsNotFound = 144
    ContentPerforceInvalidRevisionError = 145
    ContentUnloadedSaveResult = 146
    ContentPropertyInvalidNumber = 147
    ContentPropertyInvalidUrl = 148
    ContentPropertyInvalidDate = 149
    ContentPropertyInvalidSet = 150
    ContentPropertyCannotDeserialize = 151
    ContentRegexValidationFailOnProperty = 152
    ContentMaxLengthFailOnProperty = 153
    ContentPropertyUnexpectedDeserializationError = 154
    ContentPropertyRequired = 155
    ContentCannotCreateFile = 156
    ContentInvalidMigrationFile = 157
    ContentMigrationAlteringProcessedItem = 158
    ContentPropertyDefinitionNotFound = 159
    ContentReviewDataChanged = 160
    ContentRollbackRevisionNotInPackage = 161
    ContentItemNotBasedOnLatestRevision = 162
    ContentUnauthorized = 163
    ContentCannotCreateDeploymentPackage = 164
    ContentUserNotFound = 165
    ContentLocalePermissionDenied = 166
    ContentInvalidLinkToInternalEnvironment = 167
    ContentInvalidBlacklistedContent = 168
    ContentMacroMalformedNoContentId = 169
    ContentMacroMalformedNoTemplateType = 170
    ContentIllegalBNetMembershipId = 171
    ContentLocaleDidNotMatchExpected = 172
    ContentBabelCallFailed = 173
    ContentEnglishPostLiveForbidden = 174
    ContentLocaleEditPermissionDenied = 175
    UserNonUniqueName = 200
    UserManualLinkingStepRequired = 201
    UserCreateUnknownSqlResult = 202
    UserCreateUnknownSqlException = 203
    UserMalformedMembershipId = 204
    UserCannotFindRequestedUser = 205
    UserCannotLoadAccountCredentialLinkInfo = 206
    UserInvalidMobileAppType = 207
    UserMissingMobilePairingInfo = 208
    UserCannotGenerateMobileKeyWhileUsingMobileCredential = 209
    UserGenerateMobileKeyExistingSlotCollision = 210
    UserDisplayNameMissingOrInvalid = 211
    UserCannotLoadAccountProfileData = 212
    UserCannotSaveUserProfileData = 213
    UserEmailMissingOrInvalid = 214
    UserTermsOfUseRequired = 215
    UserCannotCreateNewAccountWhileLoggedIn = 216
    UserCannotResolveCentralAccount = 217
    UserInvalidAvatar = 218
    UserMissingCreatedUserResult = 219
    UserCannotChangeUniqueNameYet = 220
    UserCannotChangeDisplayNameYet = 221
    UserCannotChangeEmail = 222
    UserUniqueNameMustStartWithLetter = 223
    UserNoLinkedAccountsSupportFriendListings = 224
    UserAcknowledgmentTableFull = 225
    UserCreationDestinyMembershipRequired = 226
    UserFriendsTokenNeedsRefresh = 227
    UserEmailValidationUnknown = 228
    UserEmailValidationLimit = 229
    TransactionEmailSendFailure = 230
    MailHookPermissionFailure = 231
    MailServiceRateLimit = 232
    UserEmailMustBeVerified = 233
    UserMustAllowCustomerServiceEmails = 234
    NonTransactionalEmailSendFailure = 235
    MessagingUnknownError = 300
    MessagingSelfError = 301
    MessagingSendThrottle = 302
    MessagingNoBody = 303
    MessagingTooManyUsers = 304
    MessagingCanNotLeaveConversation = 305
    MessagingUnableToSend = 306
    MessagingDeletedUserForbidden = 307
    MessagingCannotDeleteExternalConversation = 308
    MessagingGroupChatDisabled = 309
    MessagingMustIncludeSelfInPrivateMessage = 310
    MessagingSenderIsBanned = 311
    MessagingGroupOptionalChatExceededMaximum = 312
    PrivateMessagingRequiresDestinyMembership = 313
    AddSurveyAnswersUnknownSqlException = 400
    ForumBodyCannotBeEmpty = 500
    ForumSubjectCannotBeEmptyOnTopicPost = 501
    ForumCannotLocateParentPost = 502
    ForumThreadLockedForReplies = 503
    ForumUnknownSqlResultDuringCreatePost = 504
    ForumUnknownTagCreationError = 505
    ForumUnknownSqlResultDuringTagItem = 506
    ForumUnknownExceptionCreatePost = 507
    ForumQuestionMustBeTopicPost = 508
    ForumExceptionDuringTagSearch = 509
    ForumExceptionDuringTopicRetrieval = 510
    ForumAliasedTagError = 511
    ForumCannotLocateThread = 512
    ForumUnknownExceptionEditPost = 513
    ForumCannotLocatePost = 514
    ForumUnknownExceptionGetOrCreateTags = 515
    ForumEditPermissionDenied = 516
    ForumUnknownSqlResultDuringTagIdRetrieval = 517
    ForumCannotGetRating = 518
    ForumUnknownExceptionGetRating = 519
    ForumRatingsAccessError = 520
    ForumRelatedPostAccessError = 521
    ForumLatestReplyAccessError = 522
    ForumUserStatusAccessError = 523
    ForumAuthorAccessError = 524
    ForumGroupAccessError = 525
    ForumUrlExpectedButMissing = 526
    ForumRepliesCannotBeEmpty = 527
    ForumRepliesCannotBeInDifferentGroups = 528
    ForumSubTopicCannotBeCreatedAtThisThreadLevel = 529
    ForumCannotCreateContentTopic = 530
    ForumTopicDoesNotExist = 531
    ForumContentCommentsNotAllowed = 532
    ForumUnknownSqlResultDuringEditPost = 533
    ForumUnknownSqlResultDuringGetPost = 534
    ForumPostValidationBadUrl = 535
    ForumBodyTooLong = 536
    ForumSubjectTooLong = 537
    ForumAnnouncementNotAllowed = 538
    ForumCannotShareOwnPost = 539
    ForumEditNoOp = 540
    ForumUnknownDatabaseErrorDuringGetPost = 541
    ForumExceeedMaximumRowLimit = 542
    ForumCannotSharePrivatePost = 543
    ForumCannotCrossPostBetweenGroups = 544
    ForumIncompatibleCategories = 555
    ForumCannotUseTheseCategoriesOnNonTopicPost = 556
    ForumCanOnlyDeleteTopics = 557
    ForumDeleteSqlException = 558
    ForumDeleteSqlUnknownResult = 559
    ForumTooManyTags = 560
    ForumCanOnlyRateTopics = 561
    ForumBannedPostsCannotBeEdited = 562
    ForumThreadRootIsBanned = 563
    ForumCannotUseOfficialTagCategoryAsTag = 564
    ForumAnswerCannotBeMadeOnCreatePost = 565
    ForumAnswerCannotBeMadeOnEditPost = 566
    ForumAnswerPostIdIsNotADirectReplyOfQuestion = 567
    ForumAnswerTopicIdIsNotAQuestion = 568
    ForumUnknownExceptionDuringMarkAnswer = 569
    ForumUnknownSqlResultDuringMarkAnswer = 570
    ForumCannotRateYourOwnPosts = 571
    ForumPollsMustBeTheFirstPostInTopic = 572
    ForumInvalidPollInput = 573
    ForumGroupAdminEditNonMember = 574
    ForumCannotEditModeratorEditedPost = 575
    ForumRequiresDestinyMembership = 576
    ForumUnexpectedError = 577
    ForumAgeLock = 578
    ForumMaxPages = 579
    ForumMaxPagesOldestFirst = 580
    ForumCannotApplyForumIdWithoutTags = 581
    ForumCannotApplyForumIdToNonTopics = 582
    ForumCannotDownvoteCommunityCreations = 583
    ForumTopicsMustHaveOfficialCategory = 584
    ForumRecruitmentTopicMalformed = 585
    ForumRecruitmentTopicNotFound = 586
    ForumRecruitmentTopicNoSlotsRemaining = 587
    ForumRecruitmentTopicKickBan = 588
    ForumRecruitmentTopicRequirementsNotMet = 589
    ForumRecruitmentTopicNoPlayers = 590
    ForumRecruitmentApproveFailMessageBan = 591
    ForumRecruitmentGlobalBan = 592
    ForumUserBannedFromThisTopic = 593
    ForumRecruitmentFireteamMembersOnly = 594
    ForumRequiresDestiny2Progress = 595
    GroupMembershipApplicationAlreadyResolved = 601
    GroupMembershipAlreadyApplied = 602
    GroupMembershipInsufficientPrivileges = 603
    GroupIdNotReturnedFromCreation = 604
    GroupSearchInvalidParameters = 605
    GroupMembershipPendingApplicationNotFound = 606
    GroupInvalidId = 607
    GroupInvalidMembershipId = 608
    GroupInvalidMembershipType = 609
    GroupMissingTags = 610
    GroupMembershipNotFound = 611
    GroupInvalidRating = 612
    GroupUserFollowingAccessError = 613
    GroupUserMembershipAccessError = 614
    GroupCreatorAccessError = 615
    GroupAdminAccessError = 616
    GroupPrivatePostNotViewable = 617
    GroupMembershipNotLoggedIn = 618
    GroupNotDeleted = 619
    GroupUnknownErrorUndeletingGroup = 620
    GroupDeleted = 621
    GroupNotFound = 622
    GroupMemberBanned = 623
    GroupMembershipClosed = 624
    GroupPrivatePostOverrideError = 625
    GroupNameTaken = 626
    GroupDeletionGracePeriodExpired = 627
    GroupCannotCheckBanStatus = 628
    GroupMaximumMembershipCountReached = 629
    NoDestinyAccountForClanPlatform = 630
    AlreadyRequestingMembershipForClanPlatform = 631
    AlreadyClanMemberOnPlatform = 632
    GroupJoinedCannotSetClanName = 633
    GroupLeftCannotClearClanName = 634
    GroupRelationshipRequestPending = 635
    GroupRelationshipRequestBlocked = 636
    GroupRelationshipRequestNotFound = 637
    GroupRelationshipBlockNotFound = 638
    GroupRelationshipNotFound = 639
    GroupAlreadyAllied = 641
    GroupAlreadyMember = 642
    GroupRelationshipAlreadyExists = 643
    InvalidGroupTypesForRelationshipRequest = 644
    GroupAtMaximumAlliances = 646
    GroupCannotSetClanOnlySettings = 647
    ClanCannotSetTwoDefaultPostTypes = 648
    GroupMemberInvalidMemberType = 649
    GroupInvalidPlatformType = 650
    GroupMemberInvalidSort = 651
    GroupInvalidResolveState = 652
    ClanAlreadyEnabledForPlatform = 653
    ClanNotEnabledForPlatform = 654
    ClanEnabledButCouldNotJoinNoAccount = 655
    ClanEnabledButCouldNotJoinAlreadyMember = 656
    ClanCannotJoinNoCredential = 657
    NoClanMembershipForPlatform = 658
    GroupToGroupFollowLimitReached = 659
    ChildGroupAlreadyInAlliance = 660
    OwnerGroupAlreadyInAlliance = 661
    AllianceOwnerCannotJoinAlliance = 662
    GroupNotInAlliance = 663
    ChildGroupCannotInviteToAlliance = 664
    GroupToGroupAlreadyFollowed = 665
    GroupToGroupNotFollowing = 666
    ClanMaximumMembershipReached = 667
    ClanNameNotValid = 668
    ClanNameNotValidError = 669
    AllianceOwnerNotDefined = 670
    AllianceChildNotDefined = 671
    ClanCultureIllegalCharacters = 672
    ClanTagIllegalCharacters = 673
    ClanRequiresInvitation = 674
    ClanMembershipClosed = 675
    ClanInviteAlreadyMember = 676
    GroupInviteAlreadyMember = 677
    GroupJoinApprovalRequired = 678
    ClanTagRequired = 679
    GroupNameCannotStartOrEndWithWhiteSpace = 680
    ClanCallsignCannotStartOrEndWithWhiteSpace = 681
    ClanMigrationFailed = 682
    ClanNotEnabledAlreadyMemberOfAnotherClan = 683
    GroupModerationNotPermittedOnNonMembers = 684
    ClanCreationInWorldServerFailed = 685
    ClanNotFound = 686
    ClanMembershipLevelDoesNotPermitThatAction = 687
    ClanMemberNotFound = 688
    ClanMissingMembershipApprovers = 689
    ClanInWrongStateForRequestedAction = 690
    ClanNameAlreadyUsed = 691
    ClanTooFewMembers = 692
    ClanInfoCannotBeWhitespace = 693
    GroupCultureThrottle = 694
    ClanTargetDisallowsInvites = 695
    ClanInvalidOperation = 696
    ClanFounderCannotLeaveWithoutAbdication = 697
    ClanNameReserved = 698
    ClanApplicantInClanSoNowInvited = 699
    ActivitiesUnknownException = 701
    ActivitiesParameterNull = 702
    ActivityCountsDiabled = 703
    ActivitySearchInvalidParameters = 704
    ActivityPermissionDenied = 705
    ShareAlreadyShared = 706
    ActivityLoggingDisabled = 707
    ClanRequiresExistingDestinyAccount = 750
    ClanNameRestricted = 751
    ItemAlreadyFollowed = 801
    ItemNotFollowed = 802
    CannotFollowSelf = 803
    GroupFollowLimitExceeded = 804
    TagFollowLimitExceeded = 805
    UserFollowLimitExceeded = 806
    FollowUnsupportedEntityType = 807
    NoValidTagsInList = 900
    BelowMinimumSuggestionLength = 901
    CannotGetSuggestionsOnMultipleTagsSimultaneously = 902
    NotAValidPartialTag = 903
    TagSuggestionsUnknownSqlResult = 904
    TagsUnableToLoadPopularTagsFromDatabase = 905
    TagInvalid = 906
    TagNotFound = 907
    SingleTagExpected = 908
    TagsExceededMaximumPerItem = 909
    IgnoreInvalidParameters = 1000
    IgnoreSqlException = 1001
    IgnoreErrorRetrievingGroupPermissions = 1002
    IgnoreErrorInsufficientPermission = 1003
    IgnoreErrorRetrievingItem = 1004
    IgnoreCannotIgnoreSelf = 1005
    IgnoreIllegalType = 1006
    IgnoreNotFound = 1007
    IgnoreUserGloballyIgnored = 1008
    IgnoreUserIgnored = 1009
    NotificationSettingInvalid = 1100
    PsnApiExpiredAccessToken = 1204
    PSNExForbidden = 1205
    PSNExSystemDisabled = 1218
    PsnApiErrorCodeUnknown = 1223
    PsnApiErrorWebException = 1224
    PsnApiBadRequest = 1225
    PsnApiAccessTokenRequired = 1226
    PsnApiInvalidAccessToken = 1227
    PsnApiBannedUser = 1229
    PsnApiAccountUpgradeRequired = 1230
    PsnApiServiceTemporarilyUnavailable = 1231
    PsnApiServerBusy = 1232
    PsnApiUnderMaintenance = 1233
    PsnApiProfileUserNotFound = 1234
    PsnApiProfilePrivacyRestriction = 1235
    PsnApiProfileUnderMaintenance = 1236
    PsnApiAccountAttributeMissing = 1237
    PsnApiNoPermission = 1238
    PsnApiTargetUserBlocked = 1239
    XblExSystemDisabled = 1300
    XblExUnknownError = 1301
    XblApiErrorWebException = 1302
    XblStsTokenInvalid = 1303
    XblStsMissingToken = 1304
    XblStsExpiredToken = 1305
    XblAccessToTheSandboxDenied = 1306
    XblMsaResponseMissing = 1307
    XblMsaAccessTokenExpired = 1308
    XblMsaInvalidRequest = 1309
    XblMsaFriendsRequireSignIn = 1310
    XblUserActionRequired = 1311
    XblParentalControls = 1312
    XblDeveloperAccount = 1313
    XblUserTokenExpired = 1314
    XblUserTokenInvalid = 1315
    XblOffline = 1316
    XblUnknownErrorCode = 1317
    XblMsaInvalidGrant = 1318
    ReportNotYetResolved = 1400
    ReportOverturnDoesNotChangeDecision = 1401
    ReportNotFound = 1402
    ReportAlreadyReported = 1403
    ReportInvalidResolution = 1404
    ReportNotAssignedToYou = 1405
    LegacyGameStatsSystemDisabled = 1500
    LegacyGameStatsUnknownError = 1501
    LegacyGameStatsMalformedSneakerNetCode = 1502
    DestinyAccountAcquisitionFailure = 1600
    DestinyAccountNotFound = 1601
    DestinyBuildStatsDatabaseError = 1602
    DestinyCharacterStatsDatabaseError = 1603
    DestinyPvPStatsDatabaseError = 1604
    DestinyPvEStatsDatabaseError = 1605
    DestinyGrimoireStatsDatabaseError = 1606
    DestinyStatsParameterMembershipTypeParseError = 1607
    DestinyStatsParameterMembershipIdParseError = 1608
    DestinyStatsParameterRangeParseError = 1609
    DestinyStringItemHashNotFound = 1610
    DestinyStringSetNotFound = 1611
    DestinyContentLookupNotFoundForKey = 1612
    DestinyContentItemNotFound = 1613
    DestinyContentSectionNotFound = 1614
    DestinyContentPropertyNotFound = 1615
    DestinyContentConfigNotFound = 1616
    DestinyContentPropertyBucketValueNotFound = 1617
    DestinyUnexpectedError = 1618
    DestinyInvalidAction = 1619
    DestinyCharacterNotFound = 1620
    DestinyInvalidFlag = 1621
    DestinyInvalidRequest = 1622
    DestinyItemNotFound = 1623
    DestinyInvalidCustomizationChoices = 1624
    DestinyVendorItemNotFound = 1625
    DestinyInternalError = 1626
    DestinyVendorNotFound = 1627
    DestinyRecentActivitiesDatabaseError = 1628
    DestinyItemBucketNotFound = 1629
    DestinyInvalidMembershipType = 1630
    DestinyVersionIncompatibility = 1631
    DestinyItemAlreadyInInventory = 1632
    DestinyBucketNotFound = 1633
    DestinyCharacterNotInTower = 1634
    DestinyCharacterNotLoggedIn = 1635
    DestinyDefinitionsNotLoaded = 1636
    DestinyInventoryFull = 1637
    DestinyItemFailedLevelCheck = 1638
    DestinyItemFailedUnlockCheck = 1639
    DestinyItemUnequippable = 1640
    DestinyItemUniqueEquipRestricted = 1641
    DestinyNoRoomInDestination = 1642
    DestinyServiceFailure = 1643
    DestinyServiceRetired = 1644
    DestinyTransferFailed = 1645
    DestinyTransferNotFoundForSourceBucket = 1646
    DestinyUnexpectedResultInVendorTransferCheck = 1647
    DestinyUniquenessViolation = 1648
    DestinyErrorDeserializationFailure = 1649
    DestinyValidAccountTicketRequired = 1650
    DestinyShardRelayClientTimeout = 1651
    DestinyShardRelayProxyTimeout = 1652
    DestinyPGCRNotFound = 1653
    DestinyAccountMustBeOffline = 1654
    DestinyCanOnlyEquipInGame = 1655
    DestinyCannotPerformActionOnEquippedItem = 1656
    DestinyQuestAlreadyCompleted = 1657
    DestinyQuestAlreadyTracked = 1658
    DestinyTrackableQuestsFull = 1659
    DestinyItemNotTransferrable = 1660
    DestinyVendorPurchaseNotAllowed = 1661
    DestinyContentVersionMismatch = 1662
    DestinyItemActionForbidden = 1663
    DestinyRefundInvalid = 1664
    DestinyPrivacyRestriction = 1665
    DestinyActionInsufficientPrivileges = 1666
    DestinyInvalidClaimException = 1667
    DestinyLegacyPlatformRestricted = 1668
    DestinyLegacyPlatformInUse = 1669
    DestinyLegacyPlatformInaccessible = 1670
    DestinyCannotPerformActionAtThisLocation = 1671
    DestinyThrottledByGameServer = 1672
    DestinyItemNotTransferrableHasSideEffects = 1673
    DestinyItemLocked = 1674
    DestinyCannotAffordMaterialRequirements = 1675
    DestinyFailedPlugInsertionRules = 1676
    DestinySocketNotFound = 1677
    DestinySocketActionNotAllowed = 1678
    DestinySocketAlreadyHasPlug = 1679
    DestinyPlugItemNotAvailable = 1680
    DestinyCharacterLoggedInNotAllowed = 1681
    DestinyPublicAccountNotAccessible = 1682
    DestinyClaimsItemAlreadyClaimed = 1683
    DestinyClaimsNoInventorySpace = 1684
    DestinyClaimsRequiredLevelNotMet = 1685
    DestinyClaimsInvalidState = 1686
    DestinyNotEnoughRoomForMultipleRewards = 1687
    FbInvalidRequest = 1800
    FbRedirectMismatch = 1801
    FbAccessDenied = 1802
    FbUnsupportedResponseType = 1803
    FbInvalidScope = 1804
    FbUnsupportedGrantType = 1805
    FbInvalidGrant = 1806
    InvitationExpired = 1900
    InvitationUnknownType = 1901
    InvitationInvalidResponseStatus = 1902
    InvitationInvalidType = 1903
    InvitationAlreadyPending = 1904
    InvitationInsufficientPermission = 1905
    InvitationInvalidCode = 1906
    InvitationInvalidTargetState = 1907
    InvitationCannotBeReactivated = 1908
    InvitationNoRecipients = 1910
    InvitationGroupCannotSendToSelf = 1911
    InvitationTooManyRecipients = 1912
    InvitationInvalid = 1913
    InvitationNotFound = 1914
    TokenInvalid = 2000
    TokenBadFormat = 2001
    TokenAlreadyClaimed = 2002
    TokenAlreadyClaimedSelf = 2003
    TokenThrottling = 2004
    TokenUnknownRedemptionFailure = 2005
    TokenPurchaseClaimFailedAfterTokenClaimed = 2006
    TokenUserAlreadyOwnsOffer = 2007
    TokenInvalidOfferKey = 2008
    TokenEmailNotValidated = 2009
    TokenProvisioningBadVendorOrOffer = 2010
    TokenPurchaseHistoryUnknownError = 2011
    TokenThrottleStateUnknownError = 2012
    TokenUserAgeNotVerified = 2013
    TokenExceededOfferMaximum = 2014
    TokenNoAvailableUnlocks = 2015
    TokenMarketplaceInvalidPlatform = 2016
    TokenNoMarketplaceCodesFound = 2017
    TokenOfferNotAvailableForRedemption = 2018
    TokenUnlockPartialFailure = 2019
    TokenMarketplaceInvalidRegion = 2020
    TokenOfferExpired = 2021
    RAFExceededMaximumReferrals = 2022
    RAFDuplicateBond = 2023
    RAFNoValidVeteranDestinyMembershipsFound = 2024
    RAFNotAValidVeteranUser = 2025
    RAFCodeAlreadyClaimedOrNotFound = 2026
    RAFMismatchedDestinyMembershipType = 2027
    RAFUnableToAccessPurchaseHistory = 2028
    RAFUnableToCreateBond = 2029
    RAFUnableToFindBond = 2030
    RAFUnableToRemoveBond = 2031
    RAFCannotBondToSelf = 2032
    RAFInvalidPlatform = 2033
    RAFGenerateThrottled = 2034
    RAFUnableToCreateBondVersionMismatch = 2035
    RAFUnableToRemoveBondVersionMismatch = 2036
    RAFRedeemThrottled = 2037
    NoAvailableDiscountCode = 2038
    DiscountAlreadyClaimed = 2039
    DiscountClaimFailure = 2040
    DiscountConfigurationFailure = 2041
    DiscountGenerationFailure = 2042
    DiscountAlreadyExists = 2043
    TokenRequiresCredentialXuid = 2044
    TokenRequiresCredentialPsnid = 2045
    OfferRequired = 2046
    UnknownEververseHistoryError = 2047
    MissingEververseHistoryError = 2048
    BungieRewardEmailStateInvalid = 2049
    BungieRewardNotYetClaimable = 2050
    MissingOfferConfig = 2051
    RAFQuestEntitlementRequiresBnet = 2052
    RAFQuestEntitlementTransportFailure = 2053
    RAFQuestEntitlementUnknownFailure = 2054
    RAFVeteranRewardUnknownFailure = 2055
    RAFTooEarlyToCancelBond = 2056
    LoyaltyRewardAlreadyRedeemed = 2057
    UnclaimedLoyaltyRewardEntryNotFound = 2058
    PartnerOfferPartialFailure = 2059
    PartnerOfferAlreadyClaimed = 2060
    PartnerOfferSkuNotFound = 2061
    PartnerOfferSkuExpired = 2062
    PartnerOfferPermissionFailure = 2063
    PartnerOfferNoDestinyAccount = 2064
    PartnerOfferApplyDataNotFound = 2065
    ApiExceededMaxKeys = 2100
    ApiInvalidOrExpiredKey = 2101
    ApiKeyMissingFromRequest = 2102
    ApplicationDisabled = 2103
    ApplicationExceededMax = 2104
    ApplicationDisallowedByScope = 2105
    AuthorizationCodeInvalid = 2106
    OriginHeaderDoesNotMatchKey = 2107
    AccessNotPermittedByApplicationScope = 2108
    ApplicationNameIsTaken = 2109
    RefreshTokenNotYetValid = 2110
    AccessTokenHasExpired = 2111
    ApplicationTokenFormatNotValid = 2112
    ApplicationNotConfiguredForBungieAuth = 2113
    ApplicationNotConfiguredForOAuth = 2114
    OAuthAccessTokenExpired = 2115
    ApplicationTokenKeyIdDoesNotExist = 2116
    PartnershipInvalidType = 2200
    PartnershipValidationError = 2201
    PartnershipValidationTimeout = 2202
    PartnershipAccessFailure = 2203
    PartnershipAccountInvalid = 2204
    PartnershipGetAccountInfoFailure = 2205
    PartnershipDisabled = 2206
    PartnershipAlreadyExists = 2207
    CommunityStreamingUnavailable = 2300
    TwitchNotLinked = 2500
    TwitchAccountNotFound = 2501
    TwitchCouldNotLoadDestinyInfo = 2502
    TwitchCouldNotRegisterUser = 2503
    TwitchCouldNotUnregisterUser = 2504
    TrendingCategoryNotFound = 2600
    TrendingEntryTypeNotSupported = 2601
    ReportOffenderNotInPgcr = 2700
    ReportRequestorNotInPgcr = 2701
    ReportSubmissionFailed = 2702
    ReportCannotReportSelf = 2703
    AwaTypeDisabled = 2800
    AwaTooManyPendingRequests = 2801
    AwaTheFeatureRequiresARegisteredDevice = 2802
    AwaRequestWasUnansweredForTooLong = 2803
    AwaWriteRequestMissingOrInvalidToken = 2804
    AwaWriteRequestTokenExpired = 2805
    AwaWriteRequestTokenUsageLimitReached = 2806
    SteamWebApiError = 2900
    SteamWebNullResponseError = 2901
    ClanFireteamNotFound = 3000
    ClanFireteamAddNoAlternatesForImmediate = 3001
    ClanFireteamFull = 3002
    ClanFireteamAltFull = 3003
    ClanFireteamBlocked = 3004
    ClanFireteamPlayerEntryNotFound = 3005
    ClanFireteamPermissions = 3006
    ClanFireteamInvalidPlatform = 3007
    ClanFireteamCannotAdjustSlotCount = 3008
    ClanFireteamInvalidPlayerPlatform = 3009
    ClanFireteamNotReadyForInvitesNotEnoughPlayers = 3010
    ClanFireteamGameInvitesNotSupportForPlatform = 3011
    ClanFireteamPlatformInvitePreqFailure = 3012
    ClanFireteamInvalidAuthContext = 3013
    ClanFireteamInvalidAuthProviderPsn = 3014
    ClanFireteamPs4SessionFull = 3015
    ClanFireteamInvalidAuthToken = 3016
    ClanFireteamScheduledFireteamsDisabled = 3017
    ClanFireteamNotReadyForInvitesNotScheduledYet = 3018
    ClanFireteamNotReadyForInvitesClosed = 3019
    ClanFireteamScheduledFireteamsRequireAdminPermissions = 3020
    ClanFireteamNonPublicMustHaveClan = 3021
    ClanFireteamPublicCreationRestriction = 3022
    ClanFireteamAlreadyJoined = 3023
    ClanFireteamScheduledFireteamsRange = 3024
    ClanFireteamPublicCreationRestrictionExtended = 3025
    ClanFireteamExpired = 3026
    ClanFireteamInvalidAuthProvider = 3027
    ClanFireteamInvalidAuthProviderXuid = 3028
    CrossSaveOverriddenAccountNotFound = 3200
    CrossSaveTooManyOverriddenPlatforms = 3201
    CrossSaveNoOverriddenPlatforms = 3202
    CrossSavePrimaryAccountNotFound = 3203
    CrossSaveRequestInvalid = 3204
    CrossSaveBungieAccountValidationFailure = 3206
    CrossSaveOverriddenPlatformNotAllowed = 3207
    CrossSaveThresholdExceeded = 3208
    CrossSaveIncompatibleMembershipType = 3209
    CrossSaveCouldNotFindLinkedAccountForMembershipType = 3210
    CrossSaveCouldNotCreateDestinyProfileForMembershipType = 3211
    CrossSaveErrorCreatingDestinyProfileForMembershipType = 3212
    CrossSaveCannotOverrideSelf = 3213
    CrossSaveRecentSilverPurchase = 3214
    CrossSaveSilverBalanceNegative = 3215
    CrossSaveAccountNotAuthenticated = 3216
    ErrorOneAccountAlreadyActive = 3217
    ErrorOneAccountDestinyRestriction = 3218
    CrossSaveMustMigrateToSteam = 3219
    CrossSaveSteamAlreadyPaired = 3220
    CrossSaveCannotPairJustSteamAndBlizzard = 3221
    CrossSaveCannotPairSteamAloneBeforeShadowkeep = 3222
    AuthVerificationNotLinkedToAccount = 3300
    PCMigrationMissingBlizzard = 3400
    PCMigrationMissingSteam = 3401
    PCMigrationInvalidBlizzard = 3402
    PCMigrationInvalidSteam = 3403
    PCMigrationUnknownFailure = 3404
    PCMigrationUnknownException = 3405
    PCMigrationNotLinked = 3406
    PCMigrationAccountsAlreadyUsed = 3407
    PCMigrationStepFailed = 3408
    PCMigrationInvalidBlizzardCrossSaveState = 3409
    PCMigrationDestinationBanned = 3410
    PCMigrationDestinyFailure = 3411
    PCMigrationSilverTransferFailed = 3412
    PCMigrationEntitlementTransferFailed = 3413
    PCMigrationCannotStompClanFounder = 3414
    UnsupportedBrowser = 3500
    StadiaAccountRequired = 3600

class GroupsForMemberFilter(IntEnum):
    All = 0
    Founded = 1
    NonFounded = 2

class MembershipType(IntEnum):
    Null = 0
    TigerXbox = 1
    TigerPsn = 2
    TigerSteam = 3
    TigerBlizzard = 4
    TigerStadia = 5
    TigerDemon = 10
    BungieNext = 254
    All = -1

class unpairedGameVersions(IntEnum):
    Null = 0
    Destiny2 = 1
    DLC1 = 2
    DLC2 = 4
    Forsaken = 8
    YearTwoAnnualPass = 16
    Shadowkeep = 32

class ItemBindStatus(IntEnum):
    NotBound = 0
    BoundToCharacter = 1
    BoundToAccount = 2
    BoundToGuild = 3

class TransferStatuses(IntEnum):
    CanTransfer = 0
    ItemIsEquipped = 1
    NotTransferrable = 2
    NoRoomInDestination = 4

class ItemState(IntEnum):
    Null = 0
    Locked = 1
    Tracked = 2
    Masterwork = 4

class DestinyGameVersions(IntEnum):
    Null = 0
    Destiny2 = 1
    DLC1 = 2
    DLC2 = 4
    Forsaken = 8
    YearTwoAnnualPass = 16
    Shadowkeep = 32

class DestinyComponentType(IntEnum):
    Null = 0
    Profiles = 100
    VendorReceipts = 101
    ProfileInventories = 102
    ProfileCurrencies = 103
    ProfileProgression = 104
    PlatformSilver = 105
    Characters = 200
    CharacterInventories = 201
    CharacterProgressions = 202
    CharacterRenderData = 203
    CharacterActivities = 204
    CharacterEquipment = 205
    ItemInstances = 300
    ItemObjectives = 301
    ItemPerks = 302
    ItemRenderData = 303
    ItemStats = 304
    ItemSockets = 305
    ItemTalentGrids = 306
    ItemCommonData = 307
    ItemPlugStates = 308
    ItemPlugObjectives = 309
    ItemReusablePlugs = 310
    Vendors = 400
    VendorCategories = 401
    VendorSales = 402
    Kiosks = 500
    CurrencyLookups = 600
    PresentationNodes = 700
    Collectibles = 800
    Records = 900
    Transitory = 1000
    Metrics = 1100

class ComponentPrivacySetting(IntEnum):
    Null = 0
    Public = 1
    Private = 2

class DestinyPresentationNodeState(IntEnum):
    Null = 0
    Invisible = 1
    Obscured = 2

class DestinyRecordState(IntEnum):
    Null = 0
    RecordRedeemed = 1
    RewardUnavailable = 2
    ObjectiveNotCompleted = 4
    Obscured = 8
    Invisible = 16
    EntitlementUnowned = 32
    CanEquipTitle = 64

class DestinyCollectibleState(IntEnum):
    Null = 0
    NotAcquired = 1
    Obscured = 2
    Invisible = 4
    CannotAffordMaterialRequirements = 8
    InventorySpaceUnavailable = 16
    UniquenessViolation = 32
    PurchaseDisabled = 64

class DestinyPartyMemberStates(IntEnum):
    Null = 0
    FireteamMember = 1
    PosseMember = 2
    GroupMember = 4
    PartyLeader = 8

class DestinyGamePrivacySetting(IntEnum):
    Open = 0
    ClanAndFriendsOnly = 1
    FriendsOnly = 2
    InvitationOnly = 3
    Closed = 4

class DestinyJoinClosedReasons(IntEnum):
    Null = 0
    InMatchmaking = 1
    Loading = 2
    SoloMode = 4
    InternalReasons = 8
    DisallowedByGameState = 16
    Offline = 32768

class DestinyRace(IntEnum):
    Human = 0
    Awoken = 1
    Exo = 2
    Unknown = 3

class activityModeType(IntEnum):
    Null = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    Reserved9 = 9
    Control = 10
    Reserved11 = 11
    Clash = 12
    Reserved13 = 13
    CrimsonDoubles = 15
    Nightfall = 16
    HeroicNightfall = 17
    AllStrikes = 18
    IronBanner = 19
    Reserved20 = 20
    Reserved21 = 21
    Reserved22 = 22
    Reserved24 = 24
    AllMayhem = 25
    Reserved26 = 26
    Reserved27 = 27
    Reserved28 = 28
    Reserved29 = 29
    Reserved30 = 30
    Supremacy = 31
    PrivateMatchesAll = 32
    Survival = 37
    Countdown = 38
    TrialsOfTheNine = 39
    Social = 40
    TrialsCountdown = 41
    TrialsSurvival = 42
    IronBannerControl = 43
    IronBannerClash = 44
    IronBannerSupremacy = 45
    ScoredNightfall = 46
    ScoredHeroicNightfall = 47
    Rumble = 48
    AllDoubles = 49
    Doubles = 50
    PrivateMatchesClash = 51
    PrivateMatchesControl = 52
    PrivateMatchesSupremacy = 53
    PrivateMatchesCountdown = 54
    PrivateMatchesSurvival = 55
    PrivateMatchesMayhem = 56
    PrivateMatchesRumble = 57
    HeroicAdventure = 58
    Showdown = 59
    Lockdown = 60
    Scorched = 61
    ScorchedTeam = 62
    Gambit = 63
    AllPvECompetitive = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHunt = 79
    Elimination = 80
    Momentum = 81
    Dungeon = 82
    Sundial = 83
    TrialsOfOsiris = 84

class DestinyMilestoneDisplayPreference(IntEnum):
    MilestoneDefinition = 0
    CurrentQuestSteps = 1
    CurrentActivityChallenges = 2

class DestinyMilestoneType(IntEnum):
    Unknown = 0
    Tutorial = 1
    OneTime = 2
    Weekly = 3
    Daily = 4
    Special = 5

class currentActivityModeType(IntEnum):
    Null = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    Reserved9 = 9
    Control = 10
    Reserved11 = 11
    Clash = 12
    Reserved13 = 13
    CrimsonDoubles = 15
    Nightfall = 16
    HeroicNightfall = 17
    AllStrikes = 18
    IronBanner = 19
    Reserved20 = 20
    Reserved21 = 21
    Reserved22 = 22
    Reserved24 = 24
    AllMayhem = 25
    Reserved26 = 26
    Reserved27 = 27
    Reserved28 = 28
    Reserved29 = 29
    Reserved30 = 30
    Supremacy = 31
    PrivateMatchesAll = 32
    Survival = 37
    Countdown = 38
    TrialsOfTheNine = 39
    Social = 40
    TrialsCountdown = 41
    TrialsSurvival = 42
    IronBannerControl = 43
    IronBannerClash = 44
    IronBannerSupremacy = 45
    ScoredNightfall = 46
    ScoredHeroicNightfall = 47
    Rumble = 48
    AllDoubles = 49
    Doubles = 50
    PrivateMatchesClash = 51
    PrivateMatchesControl = 52
    PrivateMatchesSupremacy = 53
    PrivateMatchesCountdown = 54
    PrivateMatchesSurvival = 55
    PrivateMatchesMayhem = 56
    PrivateMatchesRumble = 57
    HeroicAdventure = 58
    Showdown = 59
    Lockdown = 60
    Scorched = 61
    ScorchedTeam = 62
    Gambit = 63
    AllPvECompetitive = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHunt = 79
    Elimination = 80
    Momentum = 81
    Dungeon = 82
    Sundial = 83
    TrialsOfOsiris = 84

class DestinyActivityDifficultyTier(IntEnum):
    Trivial = 0
    Easy = 1
    Normal = 2
    Challenging = 3
    Hard = 4
    Brave = 5
    AlmostImpossible = 6
    Impossible = 7

class breakerType(IntEnum):
    Null = 0
    ShieldPiercing = 1
    Disruption = 2
    Stagger = 3

class EquipFailureReason(IntEnum):
    Null = 0
    ItemUnequippable = 1
    ItemUniqueEquipRestricted = 2
    ItemFailedUnlockCheck = 4
    ItemFailedLevelCheck = 8
    ItemNotOnCharacter = 16

class DestinyTalentNodeState(IntEnum):
    Invalid = 0
    CanUpgrade = 1
    NoPoints = 2
    NoPrerequisites = 3
    NoSteps = 4
    NoUnlock = 5
    NoMaterial = 6
    NoGridLevel = 7
    SwappingLocked = 8
    MustSwap = 9
    Complete = 10
    Unknown = 11
    CreationOnly = 12
    Hidden = 13

class VendorItemStatus(IntEnum):
    Success = 0
    NoInventorySpace = 1
    NoFunds = 2
    NoProgression = 4
    NoUnlock = 8
    NoQuantity = 16
    OutsidePurchaseWindow = 32
    NotAvailable = 64
    UniquenessViolation = 128
    UnknownError = 256
    AlreadySelling = 512
    Unsellable = 1024
    SellingInhibited = 2048
    AlreadyOwned = 4096
    DisplayOnly = 8192

class DestinyVendorItemState(IntEnum):
    Null = 0
    Incomplete = 1
    RewardAvailable = 2
    Complete = 4
    New = 8
    Featured = 16
    Ending = 32
    OnSale = 64
    Owned = 128
    WideView = 256
    NexusAttention = 512
    SetDiscount = 1024
    PriceDrop = 2048
    DailyOffer = 4096

class DestinySocketArrayType(IntEnum):
    Default = 0
    Intrinsic = 1

class mergeMethod(IntEnum):
    Add = 0
    Min = 1
    Max = 2

class DestinyStatsGroupType(IntEnum):
    Null = 0
    General = 1
    Weapons = 2
    Medals = 3
    ReservedGroups = 100
    Leaderboard = 101
    Activity = 102
    UniqueWeapon = 103
    Internal = 104

class DestinyStatsCategoryType(IntEnum):
    Null = 0
    Kills = 1
    Assists = 2
    Deaths = 3
    Criticals = 4
    KDa = 5
    KD = 6
    Score = 7
    Entered = 8
    TimePlayed = 9
    MedalWins = 10
    MedalGame = 11
    MedalSpecialKills = 12
    MedalSprees = 13
    MedalMultiKills = 14
    MedalAbilities = 15

class UnitType(IntEnum):
    Null = 0
    Count = 1
    PerGame = 2
    Seconds = 3
    Points = 4
    Team = 5
    Distance = 6
    Percent = 7
    Ratio = 8
    Boolean = 9
    WeaponType = 10
    Standing = 11
    Milliseconds = 12
    CompletionReason = 13

class DestinyStatsMergeMethod(IntEnum):
    Add = 0
    Min = 1
    Max = 2

class PeriodType(IntEnum):
    Null = 0
    Daily = 1
    AllTime = 2
    Activity = 3

class AwaType(IntEnum):
    Null = 0
    InsertPlugs = 1

class AwaUserSelection(IntEnum):
    Null = 0
    Rejected = 1
    Approved = 2

class AwaResponseReason(IntEnum):
    Null = 0
    Answered = 1
    TimedOut = 2
    Replaced = 3

class CommunityContentSortMode(IntEnum):
    Trending = 0
    Latest = 1
    HighestRated = 2

class TrendingEntryType(IntEnum):
    News = 0
    DestinyItem = 1
    DestinyActivity = 2
    DestinyRitual = 3
    SupportArticle = 4
    Creation = 5
    Stream = 6
    Update = 7
    Link = 8
    ForumTag = 9
    Container = 10
    Release = 11

class FireteamDateRange(IntEnum):
    All = 0
    Now = 1
    TwentyFourHours = 2
    FortyEightHours = 3
    ThisWeek = 4

class FireteamPlatform(IntEnum):
    Unknown = 0
    Playstation4 = 1
    XboxOne = 2
    Blizzard = 3
    Steam = 4
    Stadia = 5

class FireteamPublicSearchOption(IntEnum):
    PublicAndPrivate = 0
    PublicOnly = 1
    PrivateOnly = 2

class FireteamSlotSearch(IntEnum):
    NoSlotRestriction = 0
    HasOpenPlayerSlots = 1
    HasOpenPlayerOrAltSlots = 2

class FireteamPlatformInviteResult(IntEnum):
    Null = 0
    Success = 1
    AlreadyInFireteam = 2
    Throttled = 3
    ServiceError = 4

class OptInFlags(IntEnum):
    Null = 0
    Newsletter = 1
    System = 2
    Marketing = 4
    UserResearch = 8
    CustomerService = 16
    Social = 32
    PlayTests = 64
    PlayTestsLocal = 128

class GlobalAlertLevel(IntEnum):
    Unknown = 0
    Blue = 1
    Yellow = 2
    Red = 3

class GlobalAlertType(IntEnum):
    GlobalAlert = 0
    StreamingAlert = 1
