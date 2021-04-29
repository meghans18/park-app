<template>
    <div id="faq" class="container">
        <p style="color: #0a814c; font-size: 2em;">Frequently Asked Questions:</p>
        <div class="accordion" role="tablist">
            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-1 variant="success">Where can I contact the Park team?</b-button>
            </b-card-header>
            <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>You can email us anytime at <strong>assistwithpark@gmail.com</strong>! We will try our best to resolve any issues or answer any questions.</b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-2 variant="success">What locations does Park work in?</b-button>
            </b-card-header>
            <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>Park works anywhere within Iowa! When looking for a spot, just type any city name in Iowa
                            to see if there are spots located there on the day you need. We are looking to expand our offering as soon as possible.
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-6 variant="success">Why aren't any spots showing up on the map or in the list?</b-button>
            </b-card-header>
            <b-collapse id="accordion-6" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>If there are no spots on your map or in the list, there might be no spots listed as available for that date or
                    or all the spots available for that date are already reserved. Check back to see when more people have leased their spot!
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-5 variant="success">How do I rent a spot?</b-button>
            </b-card-header>
            <b-collapse id="accordion-5" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>First navigate to the <strong>Home</strong> tab. From there, you can either click on a marker on the map or on the
                            <strong>View Spot</strong> button. Either of these will take you to a page
                            that shows the spot and date you selected. You will then have to select a vehicle to proceed checking out via Stripe.
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-3 variant="success">Why isn't there a Checkout button when viewing specific spot information?</b-button>
            </b-card-header>
            <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>The checkout button will not show up unless you select a vehicle to be used in that spot during the time you rent it.
                    If there are no vehicles in the dropdown, select the <strong>Vehicles</strong> tab in the navigation bar and register your vehicle with Park first.
                    This is so that towing companies know exactly which vehicle should be in a given spot on a given day, and can tow anyone who might be in a spot that you already reserved.
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-4 variant="success">How do I list my spot for rent?</b-button>
            </b-card-header>
            <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>Due to all our payments and payouts being handled by Stripe, users must first register through Stripe before they can list a spot.
                    On the <strong>Add Spots</strong> tab, you will first see a button to connect with Stripe. Once you have done that, you will see options to list your spot 
                    or check out your Stripe dashboard to see your balance and next payout date/amount.
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>

            <b-card no-body class="mb-1">
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-button block v-b-toggle.accordion-8 variant="success">What do I do if someone stays past the day they rented my spot for?</b-button>
            </b-card-header>
            <b-collapse id="accordion-8" accordion="my-accordion" role="tabpanel">
                <b-card-body>
                <b-card-text>Please email us at <strong>assistwithpark@gmail.com</strong> right away! We will check the reservation information and then
                    contact the towing company to remove any overstay vehicles promptly.
                </b-card-text>
                </b-card-body>
            </b-collapse>
            </b-card>
        </div>
    </div>
</template>

<script>
export default {
    name: "FAQ"
}
</script>