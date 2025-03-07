# Ad-Exchanage

## Goal Calculation

Type of Goal

1. Equalized Goal Calculation : Ad-Manager, Triggered through ad-manager
2. Optiized Goal Calculation : This is Automated triggerd on the scheduled basis, One of 2 goal calculation workflows, 
results in goals based on yesterday’s delivery of non-manual ad lines in a given package.
3. Manual Goal: which is configured from Ad-Manager itself. Assumed that its goal will deliver in full.  Manual goals are not removed by any goal calculation process except when a phase ends in which case all manual goals in that phase are reset. When an ad with a manual goal is disabled it temporarily looses its manual goal until it is re-enabled and the manual goal is restored.

4. Capped Goal - A goal assigned to an ad that is lower than the original goal it received when it last went through equalized goal calculation because it could not deliver in full yesterday.

5. Capped Goal Step Up - A capped goal that achieved its lower lower goal may be increased slightly to move back towards its original equalized goal.

6. Yesterday - Midnight to midnight of the day previous to today in the campaign delivery timezone

-> What is phase ? 

package -> adline -> campaign

All Zones and All campaign

resetting the goals 

Goal -> 1k and Manual goal be like 800 then system goal be 200
but if we reset the goal then it would be 50:50.

Phases
AdLine
Capped Goal

It would take about 24 hours to run the new goal calculation logic.

And there table goal_calculation_history something where we can track like what was the old goal for this ad. and whats the new goal-calculation.

What is System goal? 
What is manual Goal?
what is automated Goal?

An ad Goal is not changing on its own?

You know it. That's why we wait 24 h because we're dealing with
daily goals at that level of abstraction, even though



Ad Line - A single ad with a start and end date that belongs to a package

Phase - A timeline with a goal that belongs to a package. The goals of all phases within a package must sum to the total package goal and phases within the same package cannot have overlapping timelines.

Package - The bridge between Ad Lines and Phases, a package contains the total goal that must be achieved by all ads that belong to it and describes the way that goal must be met over the campaign's timeline using the phases that belong to it.

Daily Goal - The total amount of impressions, clicks, or video plays (only one type) an ad line must deliver in a 24 hour period as determined by the delivery time zone of the ad line’s campaign.

System Daily Goal - A daily goal set by the automated daily goal calculation process. A system daily goal is considered “stale” when 24 hours have elapsed since its last update (the updated_at column in reporting.ad_performances).

Manual Daily Goal - A daily goal set by user input through Ad Manager. Manual goals are always projected to deliver in full when calculating goals for other non-manual goal ad lines within the same package. Manual goals are only removed by a user in Ad Manager or by the system when a phase ends. If an ad line is disabled in Ad Manager its manual goal will be restored when it is enabled again.

Capped Goal - A daily goal for an ad line that is lower than its original goal (usually equal to those running concurrently within the ad line’s package). An ad line receives a capped goal when it fails to deliver a previous day’s goal, up to the amount it could deliver on that day. An ad line with a capped goal may slowly grow back towards its original goal if it consistently meets its capped goal.

Equalized Goal Calculation - The goal calculation workflow that splits the remaining phase goal after subtracting the projected delivery of any active manual goals between ad lines with system goals. This results in equal goals assigned to active ad lines without manual goals.

Optimized Goal Calculation - The goal calculation workflow that splits the remaining phase goal after subtracting the projected delivery of any active manual goals between ad lines with system goals based on how those ad lines performed the previous day. This results in capped goals assigned to active ad lines with system goals that failed to reach their previous daily goal and to increasing the daily goal of ad lines with system goals that met their previous daily goal so that the better performing ad lines may make up for the poorer performing ad lines within the same package.

--------------------------------------------------------------
## Syncronology =>
Ad Lines ↔ Packages ↔ Phases:
Ad Lines deliver the ad content.
Packages oversee how ad lines contribute to the overarching goal.
Phases define intermediate objectives and timelines for package delivery.
For example:

A package might aim to deliver 1 million impressions across 3 months.
It splits the goal into 3 phases of 1 month each, with equal or varying goals per phase.
Multiple ad lines under the package then work toward these goals, with individual goals assigned to each ad line to ensure overall delivery success.
In essence, Ad Lines are the operational units of a campaign, directly responsible for achieving measurable results.


------------------------------------------------------------------------------------------------------------------------------------------------

Project Name: Scalabilty Engineers Pvt Ltd
My Role: Snowflake Consultant
Projetc Goal: Snowflake development and performance enhancement.

-> HeaderBiddingController
AdServiceImpl.java -> getAd(AbstaractInventoryRequest)
-> adBuys = adsFilteringService.getFilteredAdBuys(req, res, adBuys);
-> AuctionAdBuy auctionWinner = chooseAdBuy(req, res, auctionAdBuys); -> return chooseHighRpmAdBuyRecursive(req, res, auctionMix); -> AdManager -> AuctionManager
   -> dspAdProvider.hasAd() -> if (dspAdProvider.hasAd(rtbAdGroupContainer, req, res, resolvedFloorPubCurr)) {
   -> AdProvider.java -> hasAd() -> DspAdProvider.java > hasAd()
   -> dspAdRequesPopulatorFactory().getPreferredAdRequestPopulatorByBidderConfig();
   -> dspAdRequestPopulatorFactory.getDspAdRequestPopulator(bidderManager.getBidderConfig(rtbAdBuy.getBidder()));
   -> dspAdRequestPopulator.makeBidRequests(rtbRequest, req, rtbAdBuy, bidderBidRequestsMap, newFloor, bidFloorBump);
   -> makeBidRequest call makeDevice, makeImpression,	
   -> DspService -> DspServiceImpl -> getRtbAd(); ->submitBidRequest HttpPostcall to Single bidder for getdding bid in reponse to adRequest.



-> Ad ad = toAd(req, auctionWinner);
        res.setAd(ad);

# S2s Integration case where you would directly got the bidRequestPayload Ortb2

-> PublisherController.java ->zones()
-> processRequestAndSendResponse(bidRequest, request, response, out, trackingId, PROVIDER_CODE, bidRequestBody,)
-> PublisherControllerHelper.java -> processRequestAndSendResponse();
-> s2sRequestProcessingService.processBidRequest(params);
-> S2sRequestProcessingService.java -> processBidRequest()
-> getAdResponseAndLogImpression(PageRequest req) -> adService.getAd(req);
-> From here the flow wents normally


# GetPartnerData

-> VisitorServiceImpl getPartnerData
-> VistorDao -> AirospikeDBDao.java 
-> AirospikeClientManager.java -> aerospikeVisitorDao.getPartnerData(visitorId);


 vishwajeetpandey57@gmail.com

-----------------------------------------------------------------------------------------------------------------------------------------------

Date :- 28/01/2025
https://www.baeldung.com/transactions-across-microservices

https://github.com/InteractiveAdvertisingBureau/openrtb2.x/blob/main/2.6.md#example4video

---------------------------------------------------------------------------------------------------------------
# Investigation Task

AdMangerImpl -> AdDao -> AdDaoImpl 

CreativeManager- > getCreative(abBuy);
auctionManager.getMaximumRtbFloor(req.getProduct());

AuctionAdBuy rtbAdBuy
AdBuy

AdResponseServiceImpl.java

private AuctionAdBuy chooseHighestRpm(List<AuctionAdBuy> auctionMix, AdRequest req) {


The RPM value in this context likely refers to Revenue per Mille (RPM), which is a common advertising metric. It represents the estimated revenue generated per 1,000 impressions for an ad. The formula for RPM is typically:

𝑅𝑃𝑀 =(Total Revenue/Total Impressions)×1000
RPM=( Total Impressions/Total Revenue)×1000


This method, `getEffectiveRpm()`, calculates the **effective Revenue per Mille (eRPM)** for an ad auction by considering multiple revenue sources.  

---


            AdPerformance adPerformance = adPerformanceService.getAdPerformanceCachedFromS3(
                    auctionAdBuy.getId(), trackingId);

                        /**
/**
 * Defines Ad Performance related operations.
 * @author Vaibhav Puranik
 * @version $Id$
 */
public interface AdPerformanceService {
    /**
     * Returns the performance of an ad in last 12 hours.
     *      * The performance data is assumed to have been cached from S3 and may be up to 1 hour stale.
     * @param adBuyId the ad buy ID
     * @param trackingId the publisher tracking ID
     * @return the ad performance for the given tracking ID
     */
    AdPerformance getAdPerformanceCachedFromS3(Long adBuyId, String trackingId);

    /**
     * Returns the live performance of a campaign since midnight today.
     * @param campaignId the campaign ID
     * @param trackingId the publisher tracking ID
     * @return the campaign performance for the given tracking ID
     */
    CampaignPerformance getCampaignPeformanceToday(Long campaignId, String trackingId);

-----------------------------------------------------------------------------------------

/**
 * Data access object for ad performance data retrieval from S3.
 * @author Karan Dhingra
 */
public interface S3AdPerformanceDao {
    /**
     * Populates the ad performance data in a map. The keys of the map are the ad/zone cache key.
     * The value is a {@link AdPerformance} object corresponding to the key.
     * ad|tracking_id -> AdPerformance
     * ad| -> AdPerformance
     * @return
     */
    Map<String, AdPerformance> getAdPerformancesByTrackingId();





-------------------------------------------------------------------------------------------
/**
 * Views (impressions), viewable100, clicks, video plays, video completions, and revenue for a particular ad.
 * @author Vaibhav Puranik
 */
public class AdPerformance implements Serializable {
    private static final long serialVersionUID = 4800892075754167852L;

    private Long adBuyId;
    private String trackingId;
    private Long views = 0L;
    private Long overageViews = 0L;
    private Long viewable100 = 0L;
    private Long clicks = 0L;
    private Long overageClicks = 0L;
    private Long videoPlays = 0L;
    private Long overageVideoPlays = 0L;
    private Long videoCompletions = 0L;
    private Long overageVideoCompletions = 0L;
    private Long videoAutoplayPlays = 0L;
    private Long overageVideoAutoplayPlays = 0L;
    private BigDecimal revenue = BigDecimal.ZERO;
    private BigDecimal overageRevenue = BigDecimal.ZERO;
    private BigDecimal cost = BigDecimal.ZERO;
    private BigDecimal overageCost = BigDecimal.ZERO;
------------------------------------------------------------------------------------------------
### **Key Takeaways from the Code:**
1. **Initial RPM:**  
   - Starts with the base RPM (`auctionAdBuy.getRpm()`).
  
2. **Adds eRPM from RPC campaigns:**  
   - RPC (**Revenue per Click**) is multiplied by the **click-through rate** (clicks/impressions) and then scaled to per **1,000 impressions**.

3. **Adds eRPM from RPV campaigns:**  
   - RPV (**Revenue per Video Play**) is multiplied by the **video play rate** (video plays/impressions) and then scaled to per **1,000 impressions**.

4. **Handles campaigns without fixed RPM, RPC, or RPV:**  
   - If an ad has no fixed values, it retrieves **real-time revenue data** from `AdPerformance` and assigns it.

---

### **Formula Breakdown:**
- **RPM-based contribution:**  
  \[
  eRPM = RPM
  \]
  
- **RPC-based contribution:**  
  \[
  eRPM_{RPC} = \left( RPC \times \frac{\text{Clicks}}{\text{Impressions}} \right) \times 1000
  \]

- **RPV-based contribution:**  
  \[
  eRPM_{RPV} = \left( RPV \times \frac{\text{Video Plays}}{\text{Impressions}} \right) \times 1000
  \]

- **Fallback eRPM:**  
  - If **RPM, RPC, and RPV** are all **zero**, it pulls the **real-time effective RPM** from `AdPerformance`.

---

### **Purpose & Use Case:**
- This function ensures **accurate revenue estimation per 1,000 impressions** by considering **multiple revenue models**.
- Useful in **ad bidding systems, real-time ad analytics, and campaign performance tracking**.

Would you like help optimizing or modifying this logic? 🚀