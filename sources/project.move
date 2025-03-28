module MyModule::TutoringMarketplace {

    use aptos_framework::signer;
    use aptos_framework::coin;
    use aptos_framework::aptos_coin::AptosCoin;

    /// Struct representing a tutor profile.
    struct Tutor has key, store {
        rate_per_session: u64,  // Fee per session in AptosCoin
    }

    /// Function to register as a tutor with a specified session rate.
    public fun register_tutor(tutor: &signer, rate_per_session: u64) {
        move_to(tutor, Tutor { rate_per_session });
    }

    /// Function to book a session with a tutor by paying their session rate.
    public fun book_session(student: &signer, tutor_address: address) acquires Tutor {
        let tutor = borrow_global<Tutor>(tutor_address);
        let payment = coin::withdraw<AptosCoin>(student, tutor.rate_per_session);
        coin::deposit<AptosCoin>(tutor_address, payment);
    }
}
